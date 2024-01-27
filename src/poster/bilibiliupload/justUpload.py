#!/usr/bin/python3
# coding:utf8
import asyncio
import sys
import common
import engine
from engine import main
from engine.plugins.upload import bili_web
from common.Daemon import Daemon
#asyncio.run(main())
date = common.time_now()
url = "https://live.bilibili.com/734"
name = engine.config["streamers"]
name = list(name.keys())[0]
#name = "赛博朋克2077"
data = {"url":url,"date":date,"format_title":str(date)+name}
bweb = bili_web.BiliWeb(name,data,engine.config["user"])
# what is the filelist?
bweb.start()
