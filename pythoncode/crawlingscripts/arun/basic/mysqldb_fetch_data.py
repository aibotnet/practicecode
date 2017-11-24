#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'testuser', 'test123', 'testdb');

with con: 

    cur = con.cursor()
    cur.execute("SELECT * FROM Writers")

    rows = cur.fetchall()
    #print rows       #see it prints the tuples of tuple so many times we use dictionary cursor
    for row in rows:
        print row