import re
input = open('/home/aknauhwar/Desktop/json_issue/json_content_issue_test.txt','r')
output =open('/home/aknauhwar/Desktop/json_issue/json_output_1.txt','w')
lines = input.readlines()
import json

def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError, e:
    return False
  return True
  
  
def clean(str):
    str0=str.replace('\'body\'', 'doublebodydouble')
    str1=str0.replace('\'bottom_line\'', 'doublebottomlinedouble')
    str2=str1.replace('\'bullets\'', 'doublebulletsdouble')
    
    
    str3=str2.replace(': \'', 'COLON DOUBLEQUOTE')
    str40=str3.replace('\',', 'DOUBLEQUOTECOMMA')
    str4=str40.replace(': \"', 'COLON DOUBLEQUOTE')
    str50=str4.replace('\",', 'DOUBLEQUOTECOMMA')

    str5=str50.replace('\\"', 'GOODDOUBLEQUOTE')
    str6=str5.replace('\\\'', 'GOODSINGLEQUOTE')
    
    str7=str6.replace('"', '\\"')
    str8=str7.replace('\'', "\\\\\'")
    
    str9=str8.replace('doublebodydouble' , '\"body\"')
    str10=str9.replace('doublebottomlinedouble' , '\"bottom_line\"')
    str11=str10.replace('doublebulletsdouble' , '\"bullets\"')
    
    str12=str11.replace('COLON DOUBLEQUOTE' , ': \"')
    str120=str12.replace('DOUBLEQUOTECOMMA' , '\",')
    #str12=str11.replace('COLON DOUBLEQUOTE' , ': "')
    
    str13=str120.replace('GOODDOUBLEQUOTE' , '\\\\\"')
    str14=str13.replace('GOODSINGLEQUOTE' , '\\\\\'')
    
    str15=str14.replace('\\xef' , '')
    str16=str15.replace('\\xbf' , '')
    str17=str16.replace('\\xbd' , '')
    str18=str17.replace('\\xbe\\xa8' , '')
    str19=str18.replace('\\xdc\\xa2' , '')
    str20=str19.replace('\\xbe\\x8e' , '')
    
    
    return str20
    
count =0    
for line in lines:
    
            #output_string = re.sub(r'[^\d\s-]', '', line)
            #output.write(output_string)
            if "***************************" in line :
                output.write(line)
            elif "product_id:"  in line :
                output.write(line)
            
            elif "topic_id" in line :
                output.write(line)
                
            elif "content:" in line :
                cleanline=clean(line) 
                output.write(cleanline)
                str= cleanline.split("content: ")
                str1=str[1]
                #print str1
                if is_json(str1) :
                    #print str1
                    pass
                else :
                    print str1
                    count +=1
                    print count
                    #pass

                
            else : 
                pass 
                
            
                
                
                
                
                
                
                
                
                
                

            

    

output.close()
input.close()