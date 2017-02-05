#!/usr/bin/env python
# coding: utf-8
import tornado.web
import tornado.template
import logging
import stockMod
import json

class IndexHandler(tornado.web.RequestHandler):
    '''
    首页，加载Vue生成模板
    '''
    def get(self):
        self.render('dist/index.html')

# 获取股票代码列表
class stockListHandle(tornado.web.RequestHandler):
    def get(self):
        self.set_header('Content-type', 'application/json')
        codes = stockMod.get_codes_by_industry()
        self.write(json.dumps(codes))

# 获取指定代码的行情数据
class stockKlineHandle(tornado.web.RequestHandler):
    def get(self, code):
        self.set_header('Content-type', 'application/json')
        klines = stockMod.get_kline_by_code(code)
        self.write(json.dumps(klines))