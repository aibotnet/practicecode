#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import re

con = mdb.connect('10.192.169.139','','', 'spider')
input=open('/root/Arun/changedurls', "r")
lines=input.readlines()


cur = con.cursor()
with con:
     for line in lines :
               
               try:
               cur.execute( "SQL UPDATE CODE" )
               connection.commit()
               except:
               connection.rollback()





cur.close()
con.close()
input.close()
