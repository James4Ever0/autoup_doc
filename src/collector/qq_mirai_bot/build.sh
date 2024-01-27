#!/bin/bash
mkdir deps
cd MiraiGo
GOPATH=$PWD/../deps GOPROXY=https://goproxy.cn,direct go build 
