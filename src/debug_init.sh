#!/bin/bash
# the shit must be running on the background.
# how to prove?
ps aux | cat | grep node | grep chrome_receive | awk '{print $2}' | xargs -iabc  kill -s SIGKILL abc &>/dev/null
ps aux | cat | grep node | grep chrome_console | awk '{print $2}' | xargs -iabc kill -s SIGKILL abc &>/dev/null
cd collector && node chrome_receive.js &
cd collector && node chrome_console.js
cd ../
