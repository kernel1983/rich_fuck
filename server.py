
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
                (r"/add", AddHandler),
                (r"/multiply", MultiplyHandler),
            ]
        settings = {"debug": True}
        tornado.web.Application.__init__(self, handlers, **settings)

timestamp = 0
secret = 'hello'

class AddHandler(tornado.web.RequestHandler):
    task_start = 0
    def post(self):
        global timestamp

        print(self.request.body)
        data = json.loads(self.request.body)
        ts = data['timestamp']
        assert hashlib.sha256((secret+str(ts)).encode('utf8')).hexdigest() == data['otp']
        assert ts > timestamp
        timestamp = ts

        self.finish({'task':AddHandler.task_start, 'test':[
            {'input': [1, 2, 0], 'output': [0, 0, 3]},
            {'input': [2, 2, 0], 'output': [0, 0, 4]},
            {'input': [3, 2, 0], 'output': [0, 0, 5]},
        ]})
        AddHandler.task_start += 10000000

class MultiplyHandler(tornado.web.RequestHandler):
    task_start = 0
    def post(self):
        global timestamp

        print(self.request.body)
        data = json.loads(self.request.body)
        ts = data['timestamp']
        assert hashlib.sha256((secret+str(ts)).encode('utf8')).hexdigest() == data['otp']
        assert ts > timestamp
        timestamp = ts

        self.finish({'task':MultiplyHandler.task_start, 'test':[
            [[1, 2, 0], [2, 2]],
            [[2, 2, 0], [2, 4]],
            [[3, 2, 0], [2, 6]],
            [[3, 3, 0], [2, 9]],
            [[0, 0, 0], [2, 0]],
            [[-1, 1, 0], [2, -1]],
            [[-1, -1, 0], [2, 1]],
        ]})
        MultiplyHandler.task_start += 10000000

if __name__ == '__main__':
    port = sys.argv[1]
    server = Application()
    server.listen(port, '0.0.0.0')
    tornado.ioloop.IOLoop.instance().start()

