#!/usr/bin/env python
# encoding: utf-8
import pymongo
import config
import tushare as ts


client = pymongo.MongoClient(host = config.db_mongo_host, port = config.db_mongo_port)

db = client.stock

def import_codes_by_industry():
    '''
    导入行业相关的数据，不存在插入，存在更新
    '''
    collection = db.codes_industry
    # 创建索引
    collection.create_index([('code', pymongo.ASCENDING)], unique = True)
    codes = ts.get_industry_classified()
    for index, row in codes.iterrows():
        spec = {'code': row.code}
        doc = {'code': row['code'], 'name': row['name'], 'c_name': row['c_name']}
        collection.update(spec, doc, True)

def get_codes_by_industry():
    '''
    获取行业分类的股票信息
    '''
    collection = db.codes_industry
    codes = []
    for row in collection.find():
        doc = {'code': row['code'], 'name': row['name'], 'c_name': row['c_name']}
        codes.append(doc)
    return codes

def import_kline_by_code(code, ktype = 'D'):
    '''
    根据股票代码，导入股票交易行情数据
    '''
    collection = db.kline
    # 创建索引
    collection.create_index([('code', pymongo.ASCENDING), ('ktype', pymongo.ASCENDING), ('date', pymongo.ASCENDING)], unique = True)
    kline = ts.get_k_data(code, ktype=ktype)
    for index, row in kline.iterrows():
        spec = {'code': row.code, 'ktype': ktype, 'date': row.date}
        doc = {'code': row.code, 'ktype': ktype, 'date': row.date, 
        'open': row.open, 'close': row.close, 'high': row.high, 'low': row.low, 'volume': row.volume}
        collection.update(spec, doc, True)

def get_kline_by_code(code, ktype = 'D'):
    '''
    从数据库读取指定代码的kline数据
    '''
    collection = db.kline
    klines = []
    for row in collection.find({'code': code, 'ktype': ktype}).sort('date', pymongo.ASCENDING):
        row.pop('_id')
        klines.append(row)
    return klines
