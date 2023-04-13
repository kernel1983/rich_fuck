
import sys
import json
import hashlib

import tornado.web
# import tornado.websocket
import tornado.ioloop
# import tornado.gen
# import tornado.escape
# import tornado.options
# import tornado.httpserver

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
                # (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static/"}),
                # (r"/dashboard", DashboardHandler),
                # (r"/req", ReqHandler),
                # (r"/pool", PoolHandler),
                (r"/", MainHandler),
            ]
        settings = {"debug": True}
        tornado.web.Application.__init__(self, handlers, **settings)

task_start = 0
timestamp = 0
secret = 'hello'
class MainHandler(tornado.web.RequestHandler):
    def post(self):
        global timestamp
        global task_start

        print(self.request.body)
        data = json.loads(self.request.body)
        ts = data['timestamp']
        assert hashlib.sha256((secret+str(ts)).encode('utf8')).hexdigest() == data['otp']
        assert ts > timestamp
        timestamp = ts

        self.finish({'task':task_start})
        task_start += 10000000

if __name__ == '__main__':
    port = sys.argv[1]
    server = Application()
    server.listen(port, '0.0.0.0')
    tornado.ioloop.IOLoop.instance().start()

