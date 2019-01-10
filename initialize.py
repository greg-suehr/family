import os
import sqlite3

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


if __name__ == '__main__':
    initialize()
