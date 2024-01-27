#!/bin/bash
ps aux | cat | grep python3 | grep trivial_server | awk '{print $2}' | xargs -iabc  kill -s SIGKILL abc &>/dev/null
python3 trivial_server.py &
sleep 1
python3 Bilibili.py
