input = open('/home/aknauhwar/Desktop/ebay testing/EbayFinal/Fianl feb30/ebay_list_count.txt','r')

lines = input.readlines()

for line in lines[4140:] :
    if "#showing it has compability list but no list found" in line :
        
        str=line.split("    #showing it has compability")
        a=str[0] 
        print a+"      #list exist someother problem maybe showing compatibility list but none"