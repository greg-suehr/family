import sqlite3

from classes.Tables import Table

from time import sleep
from util import neat_display, check_table
from search import search

def check_safe(field, value): # TODO something sensible, safe, and sustainable
    pass 


def show(table_name, timed=True):

    if check_table(table_name):
        table = Table(table_name)  # TODO: should this load a known search order? Should we use an extant object?
        result_set = table.select_all()

        if len(result_set) != 0:
            neat_display(list(result_set))
        if timed:
            sleep(3)                       # TODO make commands more extendable, use getopt o/s


class ModelError(Exception):
    pass

def tree_display(individual_id):
    db = sqlite3.connect('family.db')
    c  = db.cursor()

    people = c.execute("select * from people where people_id = ?", str(individual_id)).fetchall()
    
    if len(people) != 1:
        raise ModelError("People should be unique, and exist.")
    
    result_set = c.execute("select * from relationships where people_1_id = ? or people_2_id = ?", str(individual_id))


def user_search(table_name, value):
    result_set = search(table_name, value)
    if result_set is not None:
        neat_display(result_set)
    else:
        print "\nNothing!"


def insert(table_name):
    '''returns first value of inserted record'''

    db = sqlite3.connect('family.db')
    c  = db.cursor()
    
    if check_table(table_name)
        fields = [_[0] for _ in c.execute('select * from %s' % table_name).description]
        inserter = {key:[] for key in fields}
        for f in fields:
            value = raw_input("%s: " % f)
            if value is "nn": return
            check_safe(f, value)
            inserter[f] = value

        insertion = [0]*len(fields)
        for i in range(len(fields)):
            insertion[i] = inserter[fields[i]]
        
        insertion = tuple(insertion)
        
        insert_sql = "insert into %s values(" % table_name + "?"  # TODO make less hacky + injection-safe
        for i in range(len(fields) - 1): insert_sql += ",?"
        insert_sql += ")"

        print insert_sql
        print insertion
        c.execute(insert_sql, insertion)

        db.commit()
        return insertion[0]
    
    else:
        print " no table called %s to insert into " % table_name
        sleep(1)

        
def associate():
    # something awful used to live here
    pass
