#!/usr/bin/python
import cgi
import cgitb
import MySQLdb as mdb

cgitb.enable()
form   = cgi.FieldStorage()                     # Get POST data

fname  = form.getfirst("fname")                 # Pull fname field data
lname  = form.getfirst("lname")                 # Pull lname field data


print "Content-Type: text/html; charset=UTF-8"  # Print headers
print ""                                        # Signal end of headers
print '''
<html>
<body>
'''


ptitle_id  = None
product_id = None

if lname is None and fname is None: #product_id is none
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
        product_id = row[0]

    query = "select nextag_ptitle_id from products where nextag_product_id=%s"
    cursor.execute(query, (a))
    row = cursor.fetchone()
    if row is not None:
        ptitle_id = row[0]

    try :
        conn.commit()
    except :
        conn.rollback()

    cursor.close()
    conn.close()




try:
    conn = mdb.connect('localhost', 'root', '', 'wize2')
except mdb.Error, e:
    print "<pre>%s</pre></body></html>" % e
    exit(1)



if lname is not None: #product_id is not none
    cursor = conn.cursor()
    product_id = lname


    count = cursor.execute("select  products.nextag_ptitle_id   from  products  where nextag_product_id =%d "
                           "for update" % (int(product_id)))

    query1 = "update products set is_bottomline = 1 , timestamp = Now() where nextag_product_id=%s"%(product_id)


    row = cursor.fetchone()
    if row is not None:
        ptitle_id=row[0]

    try :
        conn.commit()
    except :
        conn.rollback()

    cursor.close()


if fname is not None: #product_id is not none
    cursor = conn.cursor()
    ptitle_id = fname

    cursor.execute("select  products.nextag_product_id  from  products  where nextag_ptitle_id =%d "
                           "for update"%(int(ptitle_id)))

    row = cursor.fetchone()
    if row is not None:
        product_id = row[0]
        row = cursor.fetchone()

    query1 = "update products set is_bottomline = 1 , timestamp = Now() where nextag_product_id=%s"%(product_id)

    try :
        conn.commit()
    except :
        conn.rollback()

    cursor.close()




print '<form name="myform" action="./bottomline.py" method="POST">'

print '<div class="manual ptitle" >'
print '<span class="manual" style="  color: #354F59; font-family: Arial;  font-size: 15px;" >'
print "Manually feed ptitle_id: "
print '</span>'

print '<input style="width: 190px" name="fname" type="text" value=%s  />' %(str(None))

print '<input type="submit" value="submit">'
print '<span class="product_id" style="  color: #354F59; font-family: Arial;  font-size: 15px;" >'
print 'Product Id:'
print '</span>'


print '<input style="width: 110px" name="lname" type="text" value=%s />' %(product_id)
print '<span class="product_id" style="  color: #354F59; font-family: Arial;  font-size: 15px;" >'
print 'Ptitle_id:'
print '</span>'

print '<input style="width: 110px" name="pname" type="text" value=%s />' %(ptitle_id)
if ptitle_id is  not None:
	print '<iframe src="http://www.nextag.com/%d/prices-html" width="1500px" height="250px">' % (int(ptitle_id))
	print "</iframe>"



print "<br  />"
print '<br style="line-height:6px;" />'

print '<div style="overflow: auto; width:1500px; height:200px; color:#333300; border:3px solid; font-family:Arial; font-size:13px;" rows="50" cols="100">'


cursor = conn.cursor()
count =None
if product_id is not None:
	count = cursor.execute("select * from reviews where product_id= %s  " %(int(product_id)))
else:
	count = cursor.execute("select * from reviews where product_id= %s  " %(int("0")))
print '<div class="review count and name">'
print '<span class="count" style="  color: #354F59; font-family: Arial; font-size: 13px;">'
print "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+"There are %s  reviews" % (count)
print '</span>'
print '<span class="name" style=" color: #354F59; font-family: Arial; font-weight: bold; font-size: 15px;">'
print '</span>'
print '<hr noshade size=3" ></hr>'
print '</div>'


row = cursor.fetchone()




while row is not None:
    #print "<li>%s" % (row[1])
    #i=0
    results = [row[9], row[4], row[5], row[6]]
    print '<div class="rating and url">'
    print '<span class="rating" style=" color: #354F59; font-family: Arial; font-weight: bold; font-size: 15px;">'
    print "&nbsp;&nbsp;rating ::&nbsp; %s     &nbsp; &nbsp; " % (results[0])
    print '</span>'
    print '<span class="url" style="  color: #354F59; font-family: Arial; font-weight: bold; font-size: 12px;">'
    print "url&nbsp;::&nbsp;  %s" % (results[1])
    print '<span class="url">'
    print '</div>'
    print '<br style="line-height:3px;" />'
    print '<div class="title">'
    print '<strong class="strong title"  style="  color: #222222; font-family: Arial;  font-size: 13px;">'
    print "&nbsp;&nbsp;title &nbsp;::&nbsp; %s" % (results[2])
    print '</strong>'
    print '</div>'
    print '<br style="line-height:3px;" />'
    print '<div class="review text" >'
    print '<span class="text" style="  color: #354F59; font-family: Arial;  font-size: small;">'
    print "&nbsp;&nbsp;review_text &nbsp;&nbsp;:&nbsp;&nbsp;%s" % (results[3])
    print '</span>'
    print '<hr noshade size=3"></hr>'
    print '</div>'

    row = cursor.fetchone()

cursor.close()
conn.close()


print '</div>'


print '<br style="line-height:3px;" />'



print '<div class="short line" >'
print '<span class="shortline" style="  color: #354F59; font-family: Arial;  font-size: small;" >'
print "Bottomline: "
print '</span>'
print '</div>'

print '<textarea name="bottom"  style="overflow: auto; width:1500px; height:40px;" rows="50" cols="100">'
print '</textarea>'
print '<br  />'


print '<div class="long line" >'
print '<span class="longline" style="  color: #354F59; font-family: Arial;  font-size: small;" >'
print "Expert Product Review: "
print '</span>'
print '</div>'

print '<textarea name="lbottom"  style="overflow: auto; width:1500px; height:90px;" rows="50" cols="100">'

print '</textarea>'





print '<br  />'
print '<input type="submit" value="save/next" name="Submit1">'
print '<input type="submit" value="skip/next" name="Submit2">'
print '<input type="submit" value="cancel/next" name="Submit3">'

print '</form>'

print '<form style="float: right; width: 132px" name="myform1" action="./exit.py" method="POST">'
print '<input type="submit" value="exit" name="Submit4" >'
print '</form>'


print '''
</body>
</html>
'''
ptitle_id  = ''
product_id = ''
