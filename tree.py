import os
import time
import sqlite3

from commands import show, insert, associate
from collections import defaultdict

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
        elif cmd in 'build':
            associate()
        else:
            print "not implemented"

        time.sleep(1)
        os.system('clear') # clear the screen
        pass  # and execute the command


if __name__ == "__main__":
    main()
