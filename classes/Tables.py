import sqlite3

db = sqlite3.connect('family.db')
c  = db.cursor()

class Table:
    def __init__(self, table_name, search_order=[]):
        self.table_name = table_name
        self.search_order = search_order
        self.field_rules = dict()  # TODO: push as much onto the DB as you can
        self.field_messages = dict()

    def select(self, what=None, where=None):  # TODO rework where to be a dict (how to handle AND v OR?)
        """what is a list of values, where is a string (unsafe)"""

        if what is None:
            select_query = "select * from %s" % self.table_name
        else:
            select_query = "select "
            for field in what:
                select_query += "%s," % field
            select_query = select_query.rstrip(",")
            select_query += " from %s" % self.table_name

        if where is not None:
            select_query += " where %s" % where

        result_set = c.execute(select_query).fetchall()
        return result_set


    def select_all(self): return self.select(where=None)

    def insert():
        pass

    def update():
        pass

    def delete():
        pass
