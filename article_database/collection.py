from DB_management_sys import Management
from quan_tri_mang import qtm
from techtalk import tt
from tinh_te import tinh_te
from top_dev import td

import threading
import time
import sqlite3

MAX_PAGE = 7
DB_LINKS = "articles.db"


def updateDB(func):

    def inner(*args):
        management = Management(DB_LINKS)
        table_name, values = func(args)
        tbs = [i[0] for i in management.list_tables()]

        if  table_name not in  tbs:
            management.create_table(table_name)

        for i in values:
            if (
                i["link"] not in 
                [
                    i[0] for i in 
                    management.list_items("link", table=table_name)
                ]
            ):
                management.insert_item(table_name, i)

    return inner


class Collection(object):

    def add_time(self, data):
        data = list(data)

        for i in range(len(data)):
            data[i] = {
                **data[i], 
                **{"time": time.time()}
            }

        return data


    @updateDB
    def crawl_quantrimang(self, numb=0):
        _name = "QuanTriMang"
        _qtm = qtm()
        _list = ()

        for i in range(MAX_PAGE):
            _qtm.get_html_code(i)
            _list += tuple(_qtm.get_articles_attributes())

        return (_name, self[0].add_time(_list))


    @updateDB
    def crawl_techtalk(self):
        _name = "TechTalk"
        _tt = tt()
        _list = ()

        for i in range(len(_tt.url)):
            _tt.get_html_code(i)
            _list += tuple(_tt.get_articles_attributes())

        return (_name, self[0].add_time(_list))


    ''' Because of error module
    @updateDB
    def crawl_tinhte(self):
        _tt = tinh_te()
        _list = ()
        for i in range(MAX_PAGE):
            _tt.get_json_code(i)
            _list += tuple(_tt.get_articles_attributes())
        return self.add_time(_list)
    '''


    @updateDB
    def crawl_topdev(self):
        _name = "TopDev"
        _td = td()
        _list = ()

        for i in range(len(_td.url)):
            _td.get_html_code(i)
            _list += tuple(_td.get_articles_attributes())

        return (_name, self[0].add_time(_list))

