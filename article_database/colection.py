from quan_tri_mang import qtm
from techtalk import tt
from tinh_te import tinh_te
from top_dev import td

import threading
import time
import sqlite3

MAX_PAGE = 7


class Collection(object):

    def __init__(self):
        self.data = {
            "quantrimang": {},
            "techtalk": {},
            "tinhte": {},
            "topdev": {}
        }

    def add_id_and_time(self, data):
        dat = {}
        for i in tuple(data):
            dat[
                hash(
                    i[
                        list(i.keys())[0]
                    ]
                )
            ] = {**i, **{"time": time.time()}}
        return dat

    def crawl_quantrimang(self, numb=0):
        _qtm = qtm()
        _list = ()
        for i in range(MAX_PAGE):
            _qtm.get_html_code(i)
            _list += tuple(_qtm.get_articles_attributes())
        return self.add_id_and_time(_list)

    def crawl_techtalk(self):
        _tt = tt()
        _list = ()
        for i in range(len(_tt.url)):
            _tt.get_html_code(i)
            _list += tuple(_tt.get_articles_attributes())
        return self.add_id_and_time(_list)

    ''' Because of error module
    def crawl_tinhte(self):
        _tt = tinh_te()
        _list = ()
        for i in range(MAX_PAGE):
            _tt.get_json_code(i)
            _list += tuple(_tt.get_articles_attributes())
        return self.add_id_and_time(_list)
    '''

    def crawl_topdev(self):
        _td = td()
        _list = ()
        for i in range(len(_td.url)):
            _td.get_html_code(i)
            _list += tuple(_td.get_articles_attributes())
        return self.add_id_and_time(_list)

    def col(self):
        pass