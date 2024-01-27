from twisted.internet import protocol, reactor
import time
import threading
from threading import Event
import sys
import os
import re
import json
import traceback
os.system("mkdir .confidential")
global_event = Event()
questloop=["SESSDATA","bili_jct","DedeUserID"]
questpack= lambda x: ["0","background: query_cookies:{\"name\":\""+x+"\"}"]
quests=[x for z in questloop for x in questpack(z)]
# shall we leave this computer partially controllable?
# automatically run programs when not disturbed.
# the default way of building this is about making a chatroom, broadcasting all results to connected clients.
global_cookies = {}
conf_prefix = "./.confidential"
def config(obj):
    with open(conf_prefix+"/bilibili_cookies.sed","w+") as f:
        for key in obj.keys():
            sed = "s/your "+key+"/"+obj[key]+"/\n"
            f.write(sed)

def cred_dump(obj):
    obj_str = json.dumps(obj)
    with open(conf_prefix+"/bilibili_cookies.json","w+") as f:
        f.write(obj_str+"\n")
    # also execute the replace string?
class MyPP(protocol.ProcessProtocol):
    def connectionMade(self):
        pass
    def write(self, a):
        sys.stdout.buffer.write(a)
        # must display the content.
        self.transport.write(a)

    def processExited(self, reason):
        print("processExited, status %s" % (reason.value.exitCode,))

    def outReceived(self, data):
        global global_cookies, global_event
        print(data)
        # here's the key.
        decoded=data.decode()
        mreceived = "Message Received: "
        if decoded.startswith(mreceived):
            decoded = decoded[len(mreceived):-1]
            try:
                structure = json.loads(decoded)
                if "cookies" in structure.keys():
                    cookies = structure["cookies"]
                    for cookie in cookies:
                        if cookie["domain"] == ".bilibili.com":
                            if cookie["name"] not in global_cookies.keys():
                                global_cookies[cookie["name"]]=cookie["value"]
                            elif len(global_cookies.keys()) == len(questloop):
                                global_event.set()
                                # execute finalize method.
            except:
                traceback.print_exc()
            # try to decode shit.
    def errReceived(self, data):
        print("errReceived!", data)

if __name__ == "__main__":
    # multiprocessing.freeze_support()
    pp = MyPP()
    command=['./debug_init.sh']
    # check for path.
    def theFunc(a):
        a.run()
    reactor.spawnProcess(pp, command[0], command, env=os.environ, usePTY=False)
    p =threading.Thread(target=theFunc,args=(reactor,))
    p.setDaemon(True) # the whole shit.
    p.start() # not RUN!
    time.sleep(1)
    ik = 0
    while True:
        if global_event.is_set():
            cred_dump(global_cookies)
            config(global_cookies)
            break
            # finalize.
        if ik>=len(quests):
            ik%=len(quests)
        pp.write((quests[ik]+"\n").encode())
        time.sleep(1)
        ik+=1
    print("__EOL__")
    # sys.exit()
    exit()
