#!/bin/bash
config_prefix=poster/bilibiliupload
python3 cookie_getter.py
sed -f .confidential/bilibili_cookies.sed $config_prefix/config_demo.yaml > $config_prefix/config.yaml 
