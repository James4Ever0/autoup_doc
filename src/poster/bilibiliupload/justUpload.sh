#!/bin/bash
#quotes=$(ps aux | cat | grep python3 | grep trivial_server | awk '{print $2}' | wc | awk '{print $1}')
#if [ $quotes -eq 0 ]; then
#	python3 trivial_server.py &
#	sleep 1
#fi
ps aux | cat | grep bash | grep main_entrance | awk '{print $2}' | xargs -iabc  kill -s SIGKILL abc &>/dev/null
ps aux | cat | grep python3 | grep Bilibili | awk '{print $2}' | xargs -iabc  kill -s SIGKILL abc &>/dev/null
ps aux | cat | grep python3 | grep trivial_server | awk '{print $2}' | xargs -iabc  kill -s SIGKILL abc &>/dev/null
python3 trivial_server.py &
sleep 1
python3 justUpload.py
