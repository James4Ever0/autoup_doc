import requests
import urllib

target = urllib.parse.quote_plus("pappps赛博朋克")
urllib.parse.unquote_plus(target)
r = requests.get("http://localhost:9999/rename?name="+target)
print(r.text)
