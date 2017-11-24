import re
input = open('/home/aknauhwar/Desktop/json_issue/json_output _1.txt','r')
output =open('/home/aknauhwar/Desktop/json_issue/json_output_query_1.txt','w')
lines = input.readlines()
import json
#INSERT INTO product_content (product_id , topic_id , content_id) VALUES (value1,value2,value3 );
def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError, e:
    return False
  return True
count=0
insert=0
#global pid
#global tid
#global str1
pid=[]
tid=[]
str1=[]
j=0
for i in lines :
            #print i
            #j=j+1
            #global pid , tid, str1
            if "***************************" in i :
                #output.write(line)
                #insert=0
                pass
for i in lines :
            if "product_id: "  in i :
                #global pid
                #output.write(line)
                str_id=i.split("product_id: ")
                #print str_id
                pid.append(str_id[1].rstrip('\n'))
                #print pid
for i in lines :
            if "topic_id" in i :
                #global tid
                #output.write(line)
                str_tid=i.split("topic_id: ")
                tid.append(str_tid[1].rstrip('\n'))
            
for i in lines :
            if "content:" in i :
                #global str1
                #global pid
                #global tid
                #cleanline=clean(line) 
                #output.write(cleanline)
                str= i.split("content: ")
                str1.append(str[1].rstrip('\n'))
                #print str1
                if is_json(str1[count]) :
                    #print str1
                    count +=1
                    print count
           
                    #pass
                #insert=1
            
            
for i in range(0,1666) :
                output.write("REPLACE INTO product_content (product_id , topic_id , content) VALUES (%d,%d,%s );"%(int(pid[i]) , int(tid[i]) , str1[i]))
                output.write('\n')


#print pid
 
input.close()
output.close()
    