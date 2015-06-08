#!/USR/BIN/PYTHON
# -*- Ccoding : utf-8 -*-

import MySQLdb as mdb
import sys

try :
    
    con = mdb.connect('localhost','testuser','testdb','testsqldb')
    
    cur = con.cursor()
    
    cur.execute("select version()")
    
    ver= cur.fetchone()
    print "database version : %s"%(ver)
    
except mdb.Error, e :
    
    print "ERROR : %d%s"%(e.args[0],e.args[1])
    
    sys.exit(1)
    
finally :
    if con :
        con.close()
        
        