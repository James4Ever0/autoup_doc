#!/bin/bash
orig="usr/lib/python3.8/http/cookiejar.py"
src="cookiejar.py"
cp $orig $orig.bak
cp $src $orig
