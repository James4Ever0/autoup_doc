# coding: UTF-8
import sys
import os
# import time
import base64
import random
import pickle
import urllib.parse

sysrand = random.SystemRandom()

def escaped(string):
    result = urllib.parse.quote(string.encode("utf-8"))
    return result
def encoded(string):
    return base64.urlsafe_b64encode(string.encode("utf-8")).decode("utf-8")

# you would just randomly select pictures?
# nope.
def countPic(dir="celeb_pictures",minCount=100,realtime=False):
    ct=os.listdir(dir)
    ct = [x for x in ct if x.endswith(".jpeg") or x.endswith(".jpg") or x.endswith(".png")]
    lct = len(ct)
    print("total number:",lct)
    if realtime:
        return lct
    else:
        return lct<minCount

k=[]
a = sys.argv[1:]
assert len(a) == 1
# maybe it just open the shit with wrong encoding.
with open(a[0],"r", encoding='utf-8') as f:
    # k = f.read().split("\r\n")
    for line in f:
        k.append(line)
k = list(set(k))
if countPic():
    sysrand.shuffle(k)
    for x in k:
        if countPic():
        # print("picture real name",x)
            os.system("electron.cmd baidu_spider.js {}".format(encoded(x)))
        else:
            print("picture is plenty.")
else:
    print("picture is plenty.")