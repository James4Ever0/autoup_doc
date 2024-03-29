#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys
import math
import time
import json
import base64
import requests
import argparse
from requests.adapters import HTTPAdapter

# planning using two jsons. one for credential, one for video details.

# you can generate the cover anyway?

# upload flv/mp4

class Uploader(object):
    def __init__(self,cookie_string):
        # TODO: 增加登录接口使用账号密码登陆
        #  get all related shits?
        cookie = cookie_string
        self.MAX_RETRYS = 5
        self.profile = 'ugcupos/yb'
        self.cdn = 'ws'
        self.csrf = re.search('bili_jct=(.*?);', cookie + ';').group(1)
        self.mid = re.search('DedeUserID=(.*?);', cookie + ';').group(1)
        self.session = requests.session()
        self.session.mount('https://', HTTPAdapter(max_retries=self.MAX_RETRYS))
        self.session.headers['cookie'] = cookie
        self.session.headers['Accept'] = 'application/json, text/javascript, */*; q=0.01'
        self.session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
        self.session.headers['Referer'] = 'https://space.bilibili.com/{mid}/#!/'.format(mid=self.mid)


    def _upload(self, filepath):
        """执行上传文件操作"""
        if not os.path.isfile(filepath):
            print('FILE NOT EXISTS:', filepath, file=sys.stderr)
            return

        filename = os.path.basename(filepath)
        filesize = os.path.getsize(filepath)

        # 1.获取本次上传所需信息
        preupload_url = 'https://member.bilibili.com/preupload'
        params = {
            'os': 'upos',
            'r': 'upos',
            'ssl': '0',
            'name': filename,
            'size': filesize,
            'upcdn': self.cdn,
            'profile': self.profile,
        }
        response = self.session.get(preupload_url, params=params)
        upload_info = response.json()

        # 本次上传bilibili端文件名
        upload_info['bili_filename'] = upload_info['upos_uri'].split('/')[-1].split('.')[0]
        # 本次上传url
        endpoint = 'http:%s/' % upload_info['endpoint']
        upload_url = re.sub(r'^upos://', endpoint, upload_info['upos_uri'])
        print('UPLOAD URL:', upload_url, file=sys.stderr)
        # 本次上传session
        upload_session = requests.session()
        upload_session.mount('http://', HTTPAdapter(max_retries=self.MAX_RETRYS))
        upload_session.headers['X-Upos-Auth'] = upload_info['auth']

        # 2.获取本次上传的upload_id
        response = upload_session.post(upload_url + '?uploads&output=json')
        upload_info['upload_id'] = response.json()['upload_id']

        print('UPLOAD INFO:', upload_info, file=sys.stderr)

        # 3.分块上传文件
        CHUNK_SIZE = 4 * 1024 * 1024
        total_chunks = math.ceil(filesize * 1.0 / CHUNK_SIZE)
        offset = 0
        chunk = 0
        parts_info = {'parts': []}
        fp = open(filepath, 'rb')
        while True:
            blob = fp.read(CHUNK_SIZE)
            if not blob:
                break
            params = {
                'partNumber': chunk + 1,
                'uploadId': upload_info['upload_id'],
                'chunk': chunk,
                'chunks': total_chunks,
                'size': len(blob),
                'start': offset,
                'end': offset + len(blob),
                'total': filesize,
            }
            response = upload_session.put(upload_url, params=params, data=blob)
            print('Uploading...',math.floor(chunk / total_chunks  * 100), '%  UPLOAD CHUNK', chunk, ':', response.text, file=sys.stderr)

            parts_info['parts'].append({
                'partNumber': chunk + 1,
                'eTag': 'etag'
            })
            chunk += 1
            offset += len(blob)

        # 4.标记本次上传完成
        params = {
            'output': 'json',
            'name': filename,
            'profile': self.profile,
            'uploadId': upload_info['upload_id'],
            'biz_id': upload_info['biz_id']
        }
        response = upload_session.post(upload_url, params=params, data=parts_info)
        print('UPLOAD RESULT:', response.text, file=sys.stderr)

        return upload_info

    def _cover_up(self, image_path):
        """上传图片并获取图片链接"""
        if not os.path.isfile(image_path):
            return ''
        fp = open(image_path, 'rb')
        encode_data = base64.b64encode(fp.read())
        url='https://member.bilibili.com/x/vu/web/cover/up'
        data={
            'cover': b'data:image/jpeg;base64,' + encode_data,
            'csrf': self.csrf,
        }
        response = self.session.post(url, data=data)
        return response.json()['data']['url']

    def upload(self, filepath, title, tid, tag='', desc='', source='', cover_path='', dynamic='', no_reprint=1):
        """视频投稿
        Args:
            filepath   : 视频文件路径
            title      : 投稿标题
            tid        : 投稿频道id,详见https://member.bilibili.com/x/web/archive/pre
            tag        : 视频标签，多标签使用','号分隔
            desc       : 视频描述信息
            source     : 转载视频出处url
            cover_path : 封面图片路径
            dynamic    : 分享动态, 比如："#周五##放假# 劳资明天不上班"
            no_reprint : 1表示不允许转载,0表示允许
        """
        # TODO:
        # 1.增加多P上传
        # 2.对已投稿视频进行删改, 包括删除投稿，修改信息，加P删P等

        # 上传文件, 获取上传信息
        upload_info = self._upload(filepath)
        if not upload_info:
            return
        # 获取图片链接
        # cover is empty! wtf?
        # do you need to check the api? not yet. i assure you will not do this.
        cover_url = self._cover_up(cover_path) if cover_path else ''
        # 版权判断, 转载无版权
        copyright = 2 if source else 1
        # tag设置
        if isinstance(tag, list):
            tag = ','.join(tag)
        # 设置视频基本信息
        # what is that desc_format_id?
        params = {
            'copyright' : copyright,
            'source'    : source,
            'title'     : title,
            'tid'       : tid,
            'tag'       : tag,
            'no_reprint': no_reprint,
            'desc'      : desc,
            'desc_format_id': 0,
            'dynamic': dynamic,
            'cover'     : cover_url,
            'videos'    : [{
                'filename': upload_info['bili_filename'],
                'title'   : title,
                'desc'    : '',
            }]
        }
        if source:
            del params['no_reprint']
        # short for video-upload.
        url = 'https://member.bilibili.com/x/vu/web/add?csrf=' + self.csrf
        response = self.session.post(url, json=params)
        print('SET VIDEO INFO:', response.text, file=sys.stderr)
        return response.json()

def checkFile(cf):
    assert cf.startswith("/")
    assert os.path.exists(cf)
    assert os.path.isfile(cf)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='上传bilibili视频')
    parser.add_argument('-k','--json', help="full cookie dump json absolute path", required=True)
    parser.add_argument('-f', '--file', help='video file absolute path', required=True)
#    parser.add_argument('-t', '--title', help='标题', required=True)
#    parser.add_argument('-c', '--channel', type=int, help='频道id, 详见https://member.bilibili.com/x/web/archive/pre', required=True)
#    parser.add_argument('-T', '--tag', nargs='*', help='标签')
    parser.add_argument("-m","--metadata", help="json metadata of post information absolute path", required = True)
    parser.add_argument('-c', '--cover', help="cover picture absolute path")
    args = parser.parse_args()
    checkFile(args.file)
    checkFile(args.json)
    musthave = ["title","tid"]
    checkFile(args.metadata)
    parsed =None
    with open(args.metadata,"r") as fi:
        parsed = json.loads(fi.read())
    if parsed == None:
        print("metadata error")
    assert type(parsed) == dict
    key_parsed = list(parsed.keys())
    for x in musthave:
        assert x in key_parsed
    assert type(parsed["title"]) == str
    assert type(parsed["tid"]) == int
    title = parsed["title"]
    assert len(title)>0
    tid = parsed["tid"]
    tag=''
    desc=''
    source=''
    cover_path=''
    dynamic=''
    no_reprint=1
    if "tag" in key_parsed:
        assert type(parsed["tag"]) == list
        for x in parsed["tag"]:
            assert type(x) == str
            assert len(x)>0
            assert "," not in x
        tag = ",".join(parsed["tag"])
    if "desc" in key_parsed:
        assert type(parsed["desc"]) == str
        assert len(parsed["desc"])>0
        desc = parsed["desc"]
    if "source" in key_parsed:
        assert type(parsed["source"]) == str
        source = parsed["source"]
    if "cover_path" in key_parsed:
        assert type(parsed["source_path"]) == str
        checkFile(parsed["source_path"])
    if "dynamic" in key_parsed:
        assert type(parsed["dynamic"]) == dict
        ddyn = parsed["dynamic"]
        ddyn_keys = list(ddyn.keys())
        assert len(ddyn_keys) == 2
        assert "tags" in ddyn_keys
        assert "content" in ddyn_keys
        dtags = ddyn["tags"]
        dcont = ddyn["content"]
        assert type(dtags) == list
        assert type(dcont) == str
        assert len(dcont)>0
        assert "#" not in dcont
        for x in dtags:
            assert type(x) == str
            assert "#" not in x
            dynamic+="#"+x+"#"
        dynamic+=" "+dcont
    if "no_reprint" in key_parsed:
        nop = parsed["no_reprint"]
        assert type(nop) == int
        assert nop in [0,1]
        no_reprint = nop
    cookie_string = ""
    cookies = None
    with open(args.json,"r") as f:
        cookies = json.loads(f.read())
    assert type(cookies) == dict
    mustcook = ["DedeUserID", "bili_jct"]
    for x in mustcook:
        assert x in cookies.keys()
    ckeys = mustcook+[x for x in cookies.keys() if x not in mustcook]
#    assert "bili_jct" in cookies.keys()
    for x in ckeys:
        cookie_string+=x+"="+cookies[x]+"; "
    cookie_string = cookie_string[:-2]
    uper = Uploader(cookie_string)
    uper.upload(args.file, title,tid, tag=tag, desc=desc, source=source, cover_path=cover_path, dynamic=dynamic, no_reprint=no_reprint)
