__author__ = 'sudheer'
import requests
import json
import time
import datetime
from datetime import date, timedelta
import httplib, urllib2,urllib,sys,re
from bs4 import BeautifulSoup
#from BeautifulSoup import BeautifulSoup


sourceId = 2
debugValue =1
lastUpdated= 0
cityWiseDone =0
counter =0
migration =1

def lastUpdated():
    global sourceId, lastUpdated
    url = "http://54.69.171.159/api/DailyScrapping/index.php?userId=Sudheer&pass=Sudheer&method=lastUpdated&source="+str(sourceId)
    lastUpdated = urllib2.urlopen(url).read().strip()
    if not lastUpdated:
        lastUpdated =0
    if debugValue:
        print "lastUpdated :", lastUpdated


def raiseException(e):
    print e

def ignoreException(data):
    try:
        return data
    except:
        return ""

def getLinks(url , city):
    links =[]
    try:
        pageData = requests.get(url).text
    except:
        print "failed to fetch for city :",city
        print "url :", url
        return ''
    soup = BeautifulSoup(pageData)
    #tableContent = str(soup.tbody)
    data = soup.find_all("a", class_ ="adttllnk unbold")
    for attr in data:
        link = attr['href']
        link_clean = str(link.split("#")[0]).strip()
        if link_clean:
            links.append(link_clean)
    return links
                                                                                                                                                                                                                                                                                                                                                        
def getHeading(soup):
    try:
        heading = soup.find("h1", class_ ="ad_title").text.strip()
        print heading
        sys.exit()
        return heading
    except:
        return ""

def getUserName(soup):
    try:
        userName = soup.find("span", class_ ="ad-atrbt-val").text.strip()
        return userName
    except:
        return ""

def getPhoneNumber(soup):
    try:
        phone = soup.find("span", class_ ="NoVerified-Text").text.strip()
        phone = ''.join(e for e in phone if e.isalnum()) # removing extra spaces
        return phone
    except:
        return ""

def getBrand(soup):
    try:
        brand = soup.find("strong", itemprop_= "brand").text.strip()

        return brand
    except:
        return ""

def getYear(soup):
    try:
        year = soup.find("tr", class_="brbottdashc8").text.strip().split()[-1].strip()
        return year
    except:
        return ""

def checkAddedByPhone(addedInfo):
    try:
        if addedInfo.find('phone') != -1:
            return 1
        return 0
    except:
        return 0

def getAddedDate(addedInfo):
    try:
        data = addedInfo.split()
        if str(data[-1]).lower() == "pm" or str(data[-1]).lower() == "am":
            today = time.strftime("%d %b %y")
            dateValue = today+" "+data[-2]+" "+data[-1]
            timeStamp = int(time.mktime(datetime.datetime.strptime(dateValue, "%d %b %y %I:%M %p").timetuple()))
        elif str(data[-1]).lower() =="yesterday":
            yesterday = date.today() - timedelta(1)
            dateValue = yesterday.strftime('%d %b %y')
            timeStamp = int(time.mktime(datetime.datetime.strptime(dateValue, "%d %b %y").timetuple()))
        else:
            dateValue = str(data[-2]) +" "+ str(data[-1]) +" 15"
            timeStamp = int(time.mktime(datetime.datetime.strptime(dateValue, "%d %b %y").timetuple()))
        return timeStamp
    except:
        return ""

def getPrice(soup):
    try:
        price = ignoreException(soup.find("div", class_ ="pricelabel tcenter").text.strip())
        price_clean = str(re.findall('\d+',price)[0])
        return price_clean
    except:
        return ""

def getDescription(soup):
    try:
        description = soup.find("div", class_ ="ad-descbox newad-descbox ad_description_more").text.strip()
        return description
    except:
        return ""

def processLink(link , location):
    global cityWiseDone, counter, debugValue
    if debugValue:
        print link
    pageContent = requests.get(link).text
    soup = BeautifulSoup(pageContent)
    heading = getHeading(soup)
    userName = getUserName(soup)
    phone = getPhoneNumber(soup)
    brand = getBrand(soup)
    year = getYear(soup)
    price = getPrice(soup)
    description = "brand:"+str(brand)+", year :"+year+" ,"+getDescription(soup)
    try:
        addedInfo = soup.find("span", class_ ="pdingleft10 brlefte5").text.split(',')[0].strip()
        addedByPhone = checkAddedByPhone(addedInfo)
        addedOn = getAddedDate(addedInfo)
        if addedOn < lastUpdated and not migration:
            cityWiseDone = 1
            return ''
        write(userName, phone, addedOn, price, description, heading, location, addedByPhone, link)
        counter = counter +1
        if debugValue:
            print "counter :",counter
    except Exception:
        raiseException(Exception)
        pass


def insertValuation(user , phone, date, price , description,heading , locId, smartPhone, link):
    global sourceId, debugValue
    #url ="http://54.69.171.159/api/DailyScrapping/index.php?userId=Sudheer&pass=Sudheer&method=Insert&name="+str(user)+"&phone="+str(phone)+"&date="+str(date)+"&price="+str(price)+"&description="+str(description)+"&heading="+str(heading)+"&locId="+str(locId)+"&socId="+str(sourceId)+"&smartPhone="+str(smartPhone)+"&link="+str(link)
    #url = url.replace(' ', '%20')
    #if debugValue:
    #    print url
    #urllib.urlopen(url)

def getLocId(location):
    location = ''.join(e for e in location if e.isalnum())  # remove special characters and spaces
    location = location.strip().lower()
    url = "http://54.69.171.159/api/index.php?userId=Sudheer&pass=Sudheer&method=location&place="+str(location)
    url = url.replace(' ', '%20')
    locId = urllib2.urlopen(url).read()
    return str(locId.strip())

def write(user , phone, date, price , description,heading , location, smartPhone, link):
    locId = getLocId(location)
    if insertValuation(user , phone, date, price , description,heading , locId, smartPhone, link):
        return True
    else :
        return False


test_cities =0


cities = ['Mumbai', 'Bangalore', 'Chennai', 'NewDelhi', 'Hyderabad' ]

if not migration:
    lastUpdated()

urls = {'mumbai':'http://mumbai.quikr.com/Motorcycles/w1080','bangalore':'http://bangalore.quikr.com/Motorcycles/w264', 'newdelhi':'http://delhi.quikr.com/Motorcycles/w672','chennai' :'http://chennai.quikr.com/Motorcycles/w468','hyderabad':'http://hyderabad.quikr.com/Motorcycles/w774' }

if test_cities:
    for city in cities:
        url = urls[city.lower()]+"?order=timeDesc&page=1"
        links = getLinks(url,city)
        print " links : ", links
        sys.exit()


for city in cities:
    for page in range(1,200):
        if page ==1:
            url = urls[city.lower()]+"?order=timeDesc"
        else:
            url = urls[city.lower()]+"?order=timeDesc&page="+str(page)
        links = getLinks(url, city)
        if not len(links):
            break
        if debugValue:
            print "page : ",page," links : ", links
        for link in links:
            if link:
                processLink(link, city)
            if cityWiseDone:
                break
        if cityWiseDone:
            cityWiseDone =0
            break
sys.exit()

