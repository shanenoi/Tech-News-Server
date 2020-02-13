import sqlite3


class Management(object):

    def __init__(self, name):  
        self.sql = sqlite3.connect(name)
        self.cursor = self.sql.cursor()


    def create_table(self,table_name):
        self.cursor.execute(
            f"CREATE TABLE {table_name}" +
            f"( image TEXT," +
            f"  title TEXT," +
            f"  link TEXT," +
            f"  time DOUBLE )"
        )
        self.sql.commit()

    
    def list_tables(self):
        self.cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        )

        return self.cursor.fetchall()


    def insert_item(self, table, value):
        self.cursor.execute(
            f"INSERT INTO {table} VALUES(?,?,?,?)",
            (
                value["image"], value["title"], 
                value["link"], value["time"]
            )
        )
        self.sql.commit()

    
    def list_items(self, *args, table):
        self.cursor.execute(
            f"SELECT {','.join(args)} FROM {table}"
        )

        return self.cursor.fetchall()


    def end(self):
        self.cursor.close()
        self.sql.close()