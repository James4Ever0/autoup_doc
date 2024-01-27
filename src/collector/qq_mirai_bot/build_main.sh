#!/bin/bash
mkdir deps
cd go-cqhttp
GOPATH=$PWD/../deps GOPROXY=https://goproxy.cn,direct go build 
