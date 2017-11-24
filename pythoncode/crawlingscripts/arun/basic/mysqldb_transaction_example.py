#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys


try:
    con = mdb.connect('localhost', 'testuser', 'test123', 'testdb')

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Writers1")
    cur.execute("CREATE TABLE Writers1(Id INT PRIMARY KEY AUTO_INCREMENT, \
                 Name VARCHAR(25)) ENGINE=INNODB")
    cur.execute("INSERT INTO Writers1(Name) VALUES('Jack London')")
    cur.execute("INSERT INTO Writers1(Name) VALUES('Honore de Balzac')")
    cur.execute("INSERT INTO Writers1(Name) VALUES('Lion Feuchtwanger')")
    cur.execute("INSERT INTO Writers1(Name) VALUES('Emile Zola')")
    cur.execute("INSERT INTO Writers1(Name) VALUES('Truman Capote')")
    cur.execute("INSERT INTO Writers1(Name) VALUES('Terry Pratchett')")
    
    con.commit()

    
except mdb.Error, e:
  
    if con:
        con.rollback()
        
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
finally:    
            
    if con:    
        con.close()