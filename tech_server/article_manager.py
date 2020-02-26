from datetime import datetime
from random import shuffle

import sqlite3 as sql


class Article(object):

    def __init__(self, db_path):
        self.db = db_path

        self.sql = sql.connect(self.db, check_same_thread=False) # start sqlite3 connection
        self.cursor = self.sql.cursor()

        self.result = []


    def select(self, start, limit):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        result = []

        for table in self.cursor.fetchall():
            self.cursor.execute(
                f"SELECT * ,'{table[0]}' FROM {table[0]} ORDER BY time DESC LIMIT {start}, {limit};"
            )
            result += self.cursor.fetchall()

        shuffle(result)
        self.result = result


    def select_single(self, table, start, limit):
        self.cursor.execute(f"SELECT *, '{table}' FROM {table} ORDER BY time DESC LIMIT {start}, {limit};")
        self.result = self.cursor.fetchall()


    def list_table(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return [
            i[0] for i in self.cursor.fetchall()
        ]


    def format_time(self, frm_time):

        def frmt(ele):
            ele = list(ele)
            ele[-2] = datetime.utcfromtimestamp(ele[-2]).strftime(frm_time)
            return ele

        self.result = list(map(frmt, self.result))
