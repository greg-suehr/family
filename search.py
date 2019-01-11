import sqlite3

from classes import Tables

table_glob = None

def initialize():
    initialization = { 'people' : ['first_name', 'last_name', 'people_id'],
                       'places' : ['name', 'place_id'],
                       'r_types' : ['r_type', 'r_type_id'],
                       'roles' : ['role', 'role_id'],
                       'relationships' : [],  # TODO: make search                                                                                                                             
                       'note_types' : [],     #      handle these                                                                                                                             
                       'notes': ['note', 'note_id']
    }

    tables = {key: None for key in initialization.keys()}
    for k,v in initialization.iteritems():
        tables[k] = Tables.Table(table_name=k, search_order=v)


    global table_glob
    table_glob = tables

initialize()

def search(table_name, value, limit=None):    # TODO: partial searches
    """
    search a table

    table_name = string
    value      = string, int   search each field in an order specified by the Table
    value      = dict          search a specified set of columns
    limit      = int, None     the number of results to return, None returns all results

    returns a list of tuples
    """
    
    db = sqlite3.connect("family.db")  # TODO build a ROOT and relative file structure
    c = db.cursor()
    
     # TODO build a global cache for ever-searches like this                                                                                                   
    tables = [_[0] for _ in c.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()] # TODO make less hacky                                

    if table_name not in tables:
        print "No table %s to search" % tables
        return
         
    fields = [_[0] for _ in c.execute('select * from %s' % table_name).description]
    
    if type(value) is not dict:
        global table_glob
        
        for field in table_glob[table_name].search_order:
            result_set = c.execute("select * from %s where %s = ?" % (table_name, field), [value]).fetchall()  # TODO: make injection-safe
            if len(result_set) > 0:
                return result_set  # TODO: make limit work

    else:
        for i in range(len(fields)):
            pass # TODO something

         


