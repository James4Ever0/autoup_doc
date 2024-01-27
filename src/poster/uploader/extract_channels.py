import json
obj = None
def walk_type(x):
    for t in x:
        print("id:",t["id"],"name:",t["name"],"desc:",t["desc"])
        if "children" in t.keys():
            walk_type(t["children"])
def walk_fav(x):
    y = x["typelist"]
    for t in y:
        print("id:",t["id"],"name:",t["name"],"desc:",t["desc"])
def walk_staff(s):
    y = s["typelist"]
    for x in y:
        print("typeid:",x["typeid"])
        assert len(x["title_ids"]) == len(x["titles"])
        for z in range(len(x["titles"])):
            print("title:",x["titles"][z],"title_id",x["title_ids"][z])
#def 
def print_act(a):
    for x in a:
        print("id:",x["id"],"name:",x["name"],"type",x["type"],"protocol:",x["protocol"])
def print_ind(d):
    for x in d:
        print("id:",x["id"],"name:",x["name"],"type",x["type"])
def print_show(d):
    for x in d:
        print("id:",x["id"],"name:",x["name"],"type",x["type"])
def checkList(l):
    p, np = 0, 0
    for x in l:
        try:
            assert type(x) == dict
            xk = x.keys()
            assert "id" in xk
            assert "name" in xk
            assert "type" in xk
            p +=1
        except:
            np+=1
    print("passed",p,"not passed",np)
with open("channels.json","r") as f:
    obj = json.loads(f.read())
assert type(obj) == dict
d0k = obj.keys()
assert obj["code"] == 0
dt = obj["data"]
d1k = list(dt)
#['activities', 'adorders', 'fav', 'industry_list', 'myinfo', 'orders', 'prepay', 'season', 'showtype_list', 'staff_activity_conf', 'staff_conf', 'tag_rule', 'tip', 'typelist', 'video_jam', 'watermark']
lists = ["activities","adorders","industry_list","showtype_list","typelist"]
dicts = ["fav","myinfo","prepay","staff_activity_conf","staff_conf","tag_rule","tip","video_jam","watermark"]
#for x in d1k:
#    print(x, type(dt[x]))
#for x in lists:
#    print(x)
#    checkList(dt[x])
walk_type(dt["typelist"])
print_act(dt["activities"])
print_ind(dt["industry_list"])
print_show(dt["showtype_list"])
walk_fav(dt["fav"])
walk_staff(dt["staff_activity_conf"])
walk_staff(dt["staff_conf"])
