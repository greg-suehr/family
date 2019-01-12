import os
import time
import setup

from commands import show, insert, associate, user_search
from collections import defaultdict


def display():

    # TODO: implememt tree-walking display
    #   cli_display call takes root_node people_id
    #     SEARCH relationship 
    #     CALL method grow takes edge_type r_type role_id
    #     select all relationships where people_1_id = root_noe and role_2
    # ....
    
    show('relationships', timed=False)
    print
    

    
def main():
    '''Load, edit, and save a family tree'''
    
    # Don't step on an existing family tree!
    if not os.path.isfile('family.db'):
        setup.setup()

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
        elif cmd in 'search':
            table = raw_input(" search where? ")
            value = raw_input(" search what? ")
            user_search(table, value)
            raw_input(" \n any key to clear results")
        else:
            print "not implemented"

        time.sleep(2)
        os.system('clear') # clear the screen
        pass  # and execute the command


if __name__ == "__main__":
    main()
