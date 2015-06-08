#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import re

con = mdb.connect('10.192.169.139','','', 'wize2')
output=open('/root/Arun/product_id_api', "w")
with con:

    start_row=0
   # i=1 
    while 1  :
        #global i
        #i=0 
        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute("select product_id , uid ,url from url_ limit {0},1000".format(start_row)

        rows=cur.fetchall()

        if not rows :
            break


        start_row +=1000

        for row in rows:
                if not row :
                        break


                a=row['url']
                r=a.split('/')
                if 'exec' in r and len(r)==13 :

                     n=r[12].split('%')
                     s='http://www.amazon.com/product-reviews/'+n[0]
                     output.write(str(row['uid'])+'$     '  +str(row['product_id']) +'$     ' +s+'\n')

                elif 'exec'in r and len(r)==9 :

                     s='http://www.amazon.com/product-reviews/'+r[6]
                     output.write(str(row['uid'])+'$     '  +str(row['product_id']) +'$     '  +s+'\n')


                elif 'dp'in r :

                     s='http://www.amazon.com/product-reviews/'+r[4][0:10]
                     output.write(str(row['uid'])+'$     '  +str(row['product_id']) +'$     '  +s+'\n')

                elif 'gp'in r   :


                     s='http://www.amazon.com/product-reviews/'+r[5][0:10]
                     output.write(str(row['uid'])+'$     '  +str(row['product_id']) +'$     '  +s+'\n')



                else :

                     s=row['url']
                     output.write(str(row['uid'])+'$     '  +str(row['product_id']) +'$     '  +s+'\n')


output.close()
