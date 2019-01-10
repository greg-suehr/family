import sqlite3


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
            
