import os
import sqlite3

def initialize():

    db = sqlite3.connect('family.db')
    c  = db.cursor()

    c.execute("create table people (people_id INT, first_name, last_name)")

    c.execute("create table places (place_id INT, name)")

    c.execute("create table r_types  (r_type_id INT, r_type)")
    c.execute("insert into r_types values ( 1, 'filial')")
    c.execute("insert into r_types values ( 2, 'froroal')")
    c.execute("insert into r_types values ( 3, 'consanguineal')")

    c.execute("create table roles (role_id INT, role)")

    c.execute("create table relationships \                                                                            
                  (r_id INT, people_1_id INT, people_2_id INT, r_typle_id INT, role_1_id INT, role_2_id INT, place_id INT)")

    c.execute("create table note_types (note_type_id INT, note_type)")
    c.execute("insert into note_types values ( 1, 'people')")
    c.execute("insert into note_types values ( 2, 'places')")
    c.execute("insert into note_types values ( 3, 'r_types')")
    c.execute("insert into note_types values ( 4, 'relationships')")

    # A type id is one of (people_id, place_id, r_type_id, role_id, r_id)                                              
    c.execute("create table notes (note_id, note_type_id, type_id, note)")


if __name__ == '__main__':
    initialize()
