#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'testuser', 'test123', 'testdb')
    
with con:    

    cur = con.cursor()
        
    cur.execute("UPDATE Writers SET Name = %s WHERE Id = %s", 
        (" Maupasant", "3"))        
    
    print "Number of rows updated:",  cur.rowcount