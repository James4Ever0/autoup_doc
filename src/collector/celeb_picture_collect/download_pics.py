import sys
import base64
import os
import time
import urllib.parse

def now():
    return round(time.time()*1000)

ag = sys.argv[1:]
assert len(ag) == 2
assert os.path.exists(ag[0])
fpath=ag[0]
def decode(string):
    return base64.b64decode(string).decode()

fprefix = ag[1]

adds = 0 
keyword = decode(fprefix)
keyword_enc=urllib.parse.quote(keyword,"utf-8")
# use electron instead.
# do not care about duplication. it might always be true.
# just make sure the subject is not the same when rendering.