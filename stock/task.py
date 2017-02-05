#!/usr/bin/env python
# encoding: utf=8
import stockMod

def taskUpdateStockList():
    '''
    运行任务，更新股票列表
    '''
    stockMod.import_codes_by_industry()

def taskUpdateKline():
    '''
    更新所有股票的日k线数据
    '''
    codes = stockMod.get_codes_by_industry()
    for code in codes:
        stockMod.import_kline_by_code(code['code'])

taskUpdateKline()