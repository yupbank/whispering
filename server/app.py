#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import tornado.web
from apis import api_handlers
from config import DEBUG

app = tornado.web.Application(api_handlers, debug=DEBUG)

if __name__ == '__main__':
    import tornado
    import tornado.httpserver
    server = tornado.httpserver.HTTPServer(app)
    server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()

