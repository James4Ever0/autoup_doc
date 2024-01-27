import tornado.ioloop
import tornado.web
import traceback
import urllib.parse
from title_tweaker import randomSpacing, randomLeet, minmax, randomInject, randomConcat

import uuid

def tweak(name,salt=True,amount=2):
    assert type(amount) == int
    assert amount>0
    if salt:
        for x in range(amount):
            name = randomInject(name, str(uuid.uuid4())[x])
    return randomConcat(randomSpacing(randomLeet(name)," ",lambda :minmax(1,3)))

class RenameHandler(tornado.web.RequestHandler):
    def get(self):
        name = "not_right"
        try:
            name = urllib.parse.unquote_plus(self.get_query_argument("name"))
        except:
            traceback.print_exc()
#        print(dir(self))
        self.write(tweak(name))
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # shall parse url?
        self.write("/root/AGI/AutoUP/.confidential/bilibili_persistent.json")
    def make_app():
        return tornado.web.Application([(r"/rename",RenameHandler),(r"/persistent",MainHandler),])
if __name__ == "__main__":
    app = MainHandler.make_app()
    app.listen(9999)
    tornado.ioloop.IOLoop.current().start()
    exit()
    # sys.exit()
    # it works.
    # how to terminate? pid?
    # p.terminate()
    # must be thread?

