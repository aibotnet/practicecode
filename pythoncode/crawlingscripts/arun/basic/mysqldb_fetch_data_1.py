#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'testuser', 'test123', 'testdb');

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM Writers")

    for i in range(cur.rowcount):
        
        row = cur.fetchone()
        
        print row[0], row[1]
        
        '''for j in row :
                 print j  # this will print but everthing starst with anewline '''
                 
                 
