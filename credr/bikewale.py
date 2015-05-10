import urllib
import urllib2
import lxml.html as lh
import sys, traceback

#out = open('bikeDetails.txt','w')
domain="http://www.bikewale.com"

def writeData(current_brand,bike_name,bike_price,bike_km,model_year,location):
	print 'Brand Name :',current_brand
	print 'Product Name : ',bike_name
	print '---------------info----------------'
	print 'Price : ',bike_price,
	print 'KM : ',bike_km,
	print 'Model year : ',model_year
	print 'location : ',location,'\n\n\n'
	pass

def extractData(response,current_brand,url):
	tree = lh.parse(response)
	#applying xpth here for extracting information

	#for now only taking 80 bikeas from each brand
	
	for i in range (1,21):
		try:
			bike_name  = tree.xpath('//*[@id="rpgListings_pnlGrid"]/div[%s]/div[1]/a/text()'%i)[0]
			#print bike_name
	 		infolist = tree.xpath('//*[@id="rpgListings_pnlGrid"]/div[%s]/div[3]//text()'%i)
	 		#print infolist
	 		#print infolist;#break
	 		bike_price = infolist[3];bike_km = infolist[11];model_year = infolist[19]
	 		location = infolist[7]
	 		#print location;return
			writeData(current_brand,bike_name,bike_price,bike_km,model_year,location)
			#print bike_price, bike_km,model_year;
			#break
		except Exception, err:
			print Exception, err #logging exception
	
	print 'Navigating....'
	for page_no in ['2','3','4']:
		# downloding other pages for rest bikes
		response = urllib2.urlopen(url+'page-'+page_no)
		tree = lh.parse(response)
		for i in range (1,21):
			try:
				bike_name  = tree.xpath('//*[@id="rpgListings_pnlGrid"]/div[%s]/div[1]/a/text()'%i)[0]
	  			infolist = tree.xpath('//*[@id="rpgListings_pnlGrid"]/div[%s]/div[3]//text()'%i)
	  			#print infolist;#break
	  			bike_price = infolist[3];bike_km = infolist[11];model_year = infolist[19]
	  			location = infolist[7]
				writeData(current_brand,bike_name,bike_price,bike_km,model_year,location)
				#print bike_price, bike_km,model_year;#break
			except Exception, err:
				print Exception, err

	

def getPages(brand_url_set):
	for brand_url in brand_url_set:
		current_brand = brand_url.strip().split('/')[2]
		url =  domain+brand_url
		response = urllib2.urlopen(url)
		extractData(response,current_brand,url)
		#break

#
# Extract urls corresponding to brands
#
def getBrands_url(url):
	print 'Extracting brand url ...'
	brands_url=set()
	response=urllib2.urlopen(url)
	tree = lh.parse(response)
	try:
		for i in range(200): #first 200 brands
			temp = tree.xpath('//*[@id="divContent"]/ul/li[%s]/a/@href'%(i))
			#print temp
			if len(temp) > 0:
				brands_url.add(temp[0])
			#print temp
	except Exception, err:
		print Exception,err #loggong exception
	#print brands_url
	return brands_url



def scrapSite():
	#print 'Enter your city :'
	#city = raw_input()
	#print 'Budget :'
	#budget = raw_input()
	#print 'Bike Make :'
	#brand = raw_input()
	#getPages(url_string,city,budget,brand)
	brand_url_set = getBrands_url(domain+'/used/bikesbymake.aspx')
	getPages(brand_url_set) # for each brand extract all bikes

if __name__=='__main__':
	scrapSite()

