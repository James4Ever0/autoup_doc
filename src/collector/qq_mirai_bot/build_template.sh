#!/bin/bash
mkdir deps
cd MiraiGo-Template
GOPATH=$PWD/../deps GOPROXY=https://goproxy.cn,direct go build 
