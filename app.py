#!/usr/bin/env python
# coding: utf-8
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os

import stock.indexHandler

from tornado.options import define, options

define("port", default=8099, help="run on the given port", type=int)

STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static').replace('\\', '/')
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), 'templates').replace('\\', '/')

settings = {
    "static_path": STATIC_ROOT,
    "static_url_prefix": "/static/",
    'debug': True,
    "template_path": TEMPLATE_PATH,
}

handlers = [
    (r'/', stock.indexHandler.IndexHandler),
    (r'/stock/list', stock.indexHandler.stockListHandle),
    (r'/stock/kline/(.*)', stock.indexHandler.stockKlineHandle)
]

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=handlers, **settings);
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()