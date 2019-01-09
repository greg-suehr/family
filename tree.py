import os
import time
import sqlite3

from collections import defaultdict

def initialize():
    
    db = sqlite3.connect('family.db')
    c  = db.cursor()

    c.execute("create table people (people_id, first_name, last_name)")
    
    c.execute("create table places (place_id, name)")

    c.execute("create table r_types  (r_type_id, r_type)")
    c.execute("insert into r_types values ( 1, 'filial')")
    c.execute("insert into r_types values ( 2, 'froroal')")
    c.execute("insert into r_types values ( 3, 'consanguineal')")
    
    c.execute("create table roles (role_id, role)")

    c.execute("create table relationships \
                  (r_id, people_1_id, people_2_id, r_typle_id, role_1_id, role_2_id, place_id)")

    c.execute("create table note_types (note_type_id, note_type)")
    c.execute("insert into note_types values ( 1, 'people')")
    c.execute("insert into note_types values ( 2, 'places')")
    c.execute("insert into note_types values ( 3, 'r_types')")
    c.execute("insert into note_types values ( 4, 'relationships')")
    
    # A type id is one of (people_id, place_id, r_type_id, role_id, r_id)
    c.execute("create table notes (note_id, note_type_id, type_id, note)")


def display():

    # TODO: implememt tree-walking display
    #   cli_display call takes root_node people_id
    #     SEARCH relationship 
    #     CALL method grow takes edge_type r_type role_id
    #     select all relationships where people_1_id = root_noe and role_2
    # ....
    
    db = sqlite3.connect('family.db')
    c  = db.cursor()

    for i in c.execute("select * from relationships"):
        print i
        
    print
    
    return


def check_safe(field, value): # TODO something sensible, safe, and sustainable
    pass 

def show(table_name):
    db = sqlite3.connect('family.db')
    c  = db.cursor()

    # TODO build a global cache for ever-searches like this                                                                               
    tables = [_[0] for _ in c.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()] # TODO make less hacky           

    if table_name in tables:
        for i in c.execute("select * from %s" % table_name):
            print i
        print


def insert(table_name):

    db = sqlite3.connect('family.db')
    c  = db.cursor()
    
    # TODO build a global cache for ever-searches like this
    tables = [_[0] for _ in c.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()] # TODO make less hacky

    if table_name in tables:   # does this if make this injection proof?
        fields = [_[0] for _ in c.execute('select * from %s' % table_name).description]
        inserter = {key:[] for key in fields}
        for f in fields:
            value = raw_input("%s: " % f)
            check_safe(f, value)
            inserter[f] = value

        insertion = tuple(inserter.values())
        
        insert_sql = "insert into %s values(" % table_name + "?"  # TODO make less hacky
        for i in range(len(fields) - 1): insert_sql += ",?"
        insert_sql += ")"

        print insert_sql
        print insertion
        c.execute(insert_sql, insertion)
        
    else:
        print " no table called %s to insert into " % table_name
        time.sleep(1)

    db.commit()
            


def main():
    '''Load, edit, and save a family tree'''
    
    # Don't step on an existing family tree!
    if not os.path.isfile('family.db'):
        initialize()
    
    db = sqlite3.connect('family.db') # TODO: allow multiple save files
    c  = db.cursor()

    cmd = ''
    while cmd != 'quit':
        display()
        cmd = raw_input("$ ")

        if cmd in ['insert']:
            table = raw_input(" insert where? ")
            insert(table)
        elif cmd in ['show']:
            table = raw_input(" show where? ")
            show(table)
        elif cmd in 'quit':
            print 'bye!'
        else:
            print "not implemented"

        time.sleep(1)
        os.system('clear') # clear the screen
        pass  # and execute the command

    
    pass  # and execute the command


if __name__ == "__main__":
    main()
