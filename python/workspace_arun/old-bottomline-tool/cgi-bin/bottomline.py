#!/usr/bin/python
import cgi
import cgitb
import MySQLdb as mdb

cgitb.enable()


def ptitle_to_product_id(ptitle) :
    try:
        conn = mdb.connect('localhost', 'root', '', 'wize2')
    except mdb.Error, e:
        print "<pre>%s</pre></body></html>" % e
        exit(1)


    product_id=None   
    cursor = conn.cursor()
    count = cursor.execute("select  products.nextag_product_id from  products  where nextag_ptitle_id =%d and is_bottomline !=2"%(int(ptitle)))
    row = cursor.fetchone()
    #print "<ul>"
    if row is not None:
    
        product_id=row[0]
        
        row = cursor.fetchone()

    cursor.close()
    conn.close()

    return product_id




form   = cgi.FieldStorage()

button=0
if "Submit1" in form:
    button = 1
elif "Submit2" in form:
    button = 2
    
elif "Submit3" in form:
    button=3
    
elif "Submit4" in form:
    button=4

else :
    pass






short_bottomline=form.getfirst("bottom")
long_bottomline=form.getfirst("lbottom")
product_id = form.getfirst("lname")

fname  = form.getfirst("fname")                 # Pull fname field data #gets a ptitle
lname  = form.getfirst("lname")                 # Pull lname field data



initial_ptitle=0
failed_ptitle = 0    
flag = 0   
k=isinstance(fname, basestring)

if fname is None :
    fname= "Insert_ptitle_id_here"
    failed_ptitle = "Manual Ptitle insertion field was empty"
    flag=1

elif fname.isdigit() :
    initial_ptitle=fname
    


elif k is True and fname != "Insert_ptitle_id_here":
    fname = "Insert_ptitle_id_here"
    failed_ptitle = "Ptitle entered in manual insertion field was a string not a number"
    flag = 1

else :
    pass




print "Content-Type: text/html; charset=UTF-8"  # Print headers
print ""                                        # Signal end of headers

print '''
<html>
<body>
'''

if button==2 or button ==3 :
    short_bottomline=None
    long_bottomline=None

bottomline_flag=0

if (short_bottomline is not None and long_bottomline is None) or (short_bottomline is None and long_bottomline is not None) :
     bottomline_flag=1

if short_bottomline is not None and long_bottomline is not None:
    
    try:
        conn = mdb.connect('localhost', 'root', '', 'wize2')
    except mdb.Error, e:
        print "<pre>%s</pre></body></html>" % e
        exit(1)

    short_bottomline=short_bottomline.replace('\"','\\\"').replace("\'","\\\'")
    long_bottomline=long_bottomline.replace('\"','\\\"').replace("\'","\\\'")
    bottomline='{"body": "' +str(long_bottomline) +'", "bottom_line": "'+ str(short_bottomline)+'", "bullets": []}'
    cursor = conn.cursor()
    #cursor.execute("replace into  product_content (product_id , topic_id , content) values(%d,0,'%s')" % (int(product_id) , str(bottomline)))
    sql="replace into  product_content (product_id , topic_id , content) values(%s,0,%s)"
    a=int(product_id)
    b=str(bottomline)
    cursor.execute(sql ,( a, b))
    
    query = "update products set is_bottomline = 2 where nextag_product_id=%s"
    a=int(product_id)
    cursor.execute(query , ( a ) )
    try :
        conn.commit()
    except :
        conn.rollback()
    cursor.close()
    conn.close()


if fname =="Insert_ptitle_id_here":
    try:
        conn = mdb.connect('localhost','root','', 'wize2')
    
    except mdb.Error, e:
        print "<pre>%s</pre></body></html>" % e
        exit(1)
        
    cursor = conn.cursor()
    query = 'update products set is_bottomline = 0 where is_bottomline=1  and timestamp <= date_sub(now() , interval 1 hour)'


    cursor.execute("start transaction")
    query = "select  min(nextag_product_id) from products where is_bottomline = 0 and timestamp <= date_sub(now(), " \
            "interval 30 minute) for update"
    count = cursor.execute(query)

    row = cursor.fetchone()
    a =row[0]
    query1 = "update products set is_bottomline = 1 , timestamp = Now() where nextag_product_id=%s"%(a)
    cursor.execute(query1)
    cursor.execute("commit")

    if  row is not None:
        fname="Insert_ptitle_id_here"
        lname=row[0]

        
    try :
        conn.commit()
    except :
        conn.rollback()

    cursor.close()
    conn.close()
    
else:
    lname= ptitle_to_product_id(fname)
    fname="Insert_ptitle_id_here"
    



ptitle_id=None
name=None
if lname is not None:
    try:
        conn = mdb.connect('localhost', 'root', '', 'wize2')
    except mdb.Error, e:
        print "<pre>%s</pre></body></html>" % e
        exit(1)


    cursor = conn.cursor()
    cursor.execute("start transaction")
    count = cursor.execute("select  products.nextag_ptitle_id from  products  where nextag_product_id =%d for update "%(int(lname)))

    query1 = "update products set is_bottomline = 1 , timestamp = Now() where nextag_product_id=%s"%(lname)
    cursor.execute("commit")
    row = cursor.fetchone()
    
    if row is not None:
        ptitle_id=row[0]
        row = cursor.fetchone()

    try :
        conn.commit()
    except :
        conn.rollback()

    cursor.close()
    conn.close()




Not_Found=0
if ptitle_id is None:
    Not_Found=1
    try:
        conn = mdb.connect('localhost', 'root', '', 'wize2')
    except mdb.Error, e:
        print "<pre>%s</pre></body></html>" % e
        exit(1)
        
    cursor = conn.cursor()
    query = 'update products set is_bottomline = 0 where is_bottomline=1  and timestamp <= date_sub(now() , interval 1 hour)'
    cursor.execute(query)

    cursor.execute("start transaction")
    query = "select  min(nextag_product_id) from products where is_bottomline = 0 and timestamp <= date_sub(now(), " \
            "interval 30 minute) for update"
    count = cursor.execute(query)

    row = cursor.fetchone()
    a =row[0]
    query1 = "update products set is_bottomline = 1 , timestamp = Now() where nextag_product_id=%s"%(a)
    cursor.execute(query1)
    cursor.execute("commit")

    
    if row is not None:
        fname="Insert_ptitle_id_here"
        lname=row[0]

    try :
        conn.commit()
    except :
        conn.rollback()
        
         
    #print "</ul>"
    cursor.close()
    conn.close()
    

    
if Not_Found== 1 and lname is not None:
    flag=1
    failed_ptitle="Manually inserted ptitle_id =%s was not found in database , check if it was correctly inserted \n " \
                  "Random product generated"%(str(initial_ptitle))

    try:
        conn = mdb.connect('localhost', 'root', '', 'wize2')
    except mdb.Error, e:
        print "<pre>%s</pre></body></html>" % e
        exit(1)
        
    cursor = conn.cursor()
    count = cursor.execute("select  products.nextag_ptitle_id  from  products  where nextag_product_id =%d for update"%(int(lname)))
    query1 = "update products set is_bottomline = 1 , timestamp = Now() where nextag_product_id=%s"%(lname)

    row = cursor.fetchone()
    if row is not None:
        ptitle_id=row[0]

    cursor.close()
    conn.close()
    



print '<form name="myform" action="./bottomline.py" method="POST">'
#print "Manually feed ptitle_id: "

print '<div class="manual ptitle" >'
print '<span class="manual" style="  color: #354F59; font-family: Arial;  font-size: 15px;" >'
print "Manually feed ptitle_id: "
print '</span>'

#print "<br  />"
print '<input style="width: 190px" name="fname" type="text" value=%s  />' %(str(fname))
#print '<br  />'
print '<input type="submit" value="submit">'


print '<span class="product_id" style="  color: #354F59; font-family: Arial;  font-size: 15px;" >'
print 'Product Id:'
print '</span>'





#print '<br  />'
print '<input style="width: 110px" name="lname" type="text" value=%s />' %(lname)

#print 'Ptitle_id:'
print '<span class="product_id" style="  color: #354F59; font-family: Arial;  font-size: 15px;" >'
print 'Ptitle_id:'
print '</span>'




print '<input style="width: 110px" name="pname" type="text" value=%s />' %(ptitle_id)

print '</div>'


if flag :
    print '<div class="error and validation">'
    #print '<hr noshade size=3" ></hr>'
    print '<span class="name" style=" color: #FF0000; font-family: Arial; font-weight: bold; font-size: 15px;">'
    #print '&nbsp;&nbsp;'*56+'NOTE&nbsp;::&nbsp;%s'%(str(failed_ptitle))
    print '<center>NOTE&nbsp;::&nbsp;%s</center>'%(str(failed_ptitle))
    print '</span>'
    #print '<hr noshade size=3" ></hr>'
    print '</div>'
    
if bottomline_flag==1 :
    print '<div class="error and validation of bottomline">'
    #print '<hr noshade size=3" ></hr>'
    print '<span class="bottomline_failure" style=" color: #FF0000; font-family: Arial; font-weight: bold; font-size: 15px;">'
    #print '&nbsp;&nbsp;'*56+'NOTE&nbsp;::&nbsp;%s'%(str(failed_ptitle))
    print '<center>Please check .... Last submitted bottomline was incomplete </center>'
    print '</span>'
    #print '<hr noshade size=3" ></hr>'
    print '</div>'
    

    
print '<iframe src="http://www.nextag.com/%d/prices-html" width="1500px" height="250px">'%(int(ptitle_id))
print "</iframe>"


    



    

    
    
    

#print '<input type="submit" value="submit">'
#print '</form>'
#print '<br  />'


try:

    conn = mdb.connect('localhost','root','', 'wize2')

except mdb.Error, e:
    print "<pre>%s</pre></body></html>" % e
    exit(1)

#print "Reviews: "
print "<br  />"
print '<br style="line-height:6px;" />'


#print '<textarea style="overflow: auto; width:1500px; height:315px;" rows="50" cols="100">'
print '<div style="overflow: auto; width:1500px; height:200px; color:#333300; border:3px solid; font-family:Arial; font-size:13px;" rows="50" cols="100">'

cursor = conn.cursor()
count = cursor.execute("select * from reviews where product_id= %s  " %(lname))
#count = cursor.execute("select * from reviews where product_id= %s for update " %(lname))



    


print '<div class="review count and name">'
print '<span class="count" style="  color: #354F59; font-family: Arial; font-size: 13px;">'
print "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+"There are %s  reviews" % (count)
print '</span>'
print '<span class="name" style=" color: #354F59; font-family: Arial; font-weight: bold; font-size: 15px;">'
print "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Product_name=%s"%(name)
print '</span>'
print '<hr noshade size=3" ></hr>'
print '</div>'
#print "<br  />"
#print"***********************************new review****************************************"

#print "<br  />"
row = cursor.fetchone()
#print "<ul>"


while row is not None:
    #print "<li>%s" % (row[1])
    #i=0
    results=[row[9],row[4] ,row[5] , row[6]]
    
    print '<div class="rating and url">'
    
    print '<span class="rating" style=" color: #354F59; font-family: Arial; font-weight: bold; font-size: 15px;">'
    print "&nbsp;&nbsp;rating ::&nbsp; %s     &nbsp; &nbsp; " % (results[0])
    print '</span>'
    
    print '<span class="url" style="  color: #354F59; font-family: Arial; font-weight: bold; font-size: 12px;">'
    print "url&nbsp;::&nbsp;  %s" % (results[1])
    print '<span class="url">'
    
    print '</div>'
    #print "<br  />"
    print '<br style="line-height:3px;" />'
    
    print '<div class="title">'
    print '<strong class="strong title"  style="  color: #222222; font-family: Arial;  font-size: 13px;">'
    print "&nbsp;&nbsp;title &nbsp;::&nbsp; %s" % (results[2])
    print '</strong>'
    print '</div>'
    
    print '<br style="line-height:3px;" />'
    #print "<br  />"
    
    print '<div class="review text" >'
    print '<span class="text" style="  color: #354F59; font-family: Arial;  font-size: small;">'
    print "&nbsp;&nbsp;review_text &nbsp;&nbsp;:&nbsp;&nbsp;%s" % (results[3])
    print '</span>'
    #print "<br  />"
    #print"***********************************new review****************************************"
    print '<hr noshade size=3"></hr>'
    print '</div>'
    #print "<br  />"

    #i +=1


    row = cursor.fetchone()
    
#print "</ul>"
cursor.close()
conn.close()


#print '<textarea rows="10" cols="30">'
#print "The cat was playing in the garden."
#print '</textarea>'
print '</div>'

#print "<br  />"
#print "Manual product_id:",fname
#print "<br  />"
#print "Product Id:",lname
#print "<br  />"
#print "Whole Info:",str(fname)+" "+str(lname)
#print "<br  />"
#print "The secret was:",secret

#print '<form name="myformbottomline" action="./bottomline.py" method="POST">'
#print '<br  />'

print '<br style="line-height:3px;" />'

print '<div class="short line" >'
print '<span class="shortline" style="  color: #354F59; font-family: Arial;  font-size: small;" >'
print "Bottomline: "
print '</span>'
print '</div>'


print '<textarea name="bottom"  style="overflow: auto; width:1500px; height:40px;" rows="50" cols="100">'
#print "write your bottomline here ...."
#print "Not all those who wander are lost...."
print '</textarea>'

print '<br  />'


#print "Expert Product Review: "
print '<div class="long line" >'
print '<span class="longline" style="  color: #354F59; font-family: Arial;  font-size: small;" >'
print "Expert Product Review: "
print '</span>'
print '</div>'

print '<textarea name="lbottom"  style="overflow: auto; width:1500px; height:90px;" rows="50" cols="100">'
#print "write your bottomline here ...."
#print "Not all those who wander are lost...."
print '</textarea>'

print '<br  />'
print '<input type="submit" value="save/next" name="Submit1">'
print '<input type="submit" value="skip/next" name="Submit2">'
print '<input type="submit" value="cancel/next" name="Submit3">'
#print '<input type="submit" value="exit" name="Submit4" action="./exit.py" method="POST">'
print '</form>'

print '<form style="float: right; width: 132px" name="myform1" action="./exit.py" method="POST">'
print '<input type="submit" value="exit" name="Submit4" >'
print '</form>'


print '''
</body>
</html>
'''
