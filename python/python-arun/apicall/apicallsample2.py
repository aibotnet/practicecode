#Send Content-type header to browser
print "Content-type: text/html"
print
 
#import the HTTP, DOM and ConfigParser modules needed
import httplib, ConfigParser
from xml.dom.minidom import parse, parseString
 

# open config file
config = ConfigParser.ConfigParser()
config.read("/home/aknauhwar/python/apicall/config1.ini")
 
# specify eBay API dev,app,cert IDs
devID = config.get("Keys", "Developer")
appID = config.get("Keys", "Application")
certID = config.get("Keys", "Certificate")


#get the server details from the config file
serverUrl = config.get("Server", "URL")
serverDir = config.get("Server", "Directory")
 
 
# specify eBay token
# note that eBay requires encrypted storage of user data
userToken = config.get("Authentication", "Token")
 
 
#eBay Call Variables
#siteID specifies the eBay international site to associate the call with
#0 = US, 2 = Canada, 3 = UK, ....
siteID = "100"
#verb specifies the name of the call
verb = "getProductCompatibilities"
#The API level that the application conforms to
compatabilityLevel = "747"  #try 851
 
 
#Setup the HTML Page with name of call as title
print "<HTML>"
print "<HEAD><TITLE>", verb, "</TITLE></HEAD>"
print "<BODY>"
 
 
 
 
# FUNCTION: buildHttpHeaders
# Build together the required headers for the HTTP request to the eBay API
def buildHttpHeaders():
    httpHeaders = {"X-EBAY-API-COMPATIBILITY-LEVEL": compatabilityLevel,
               "X-EBAY-API-DEV-NAME": devID,
               "X-EBAY-API-APP-NAME": appID,
               "X-EBAY-API-CERT-NAME": certID,
               "X-EBAY-API-CALL-NAME": verb,
               "X-EBAY-API-SITEID": siteID,
               "Content-Type": "text/xml"}
    return httpHeaders
 
# FUNCTION: buildRequestXml
# Build the body of the call (in XML) incorporating the required parameters to pass
def buildRequestXml():
    
    requestXml ="<?xml version='1.0' encoding='UTF-8'?>"+\
                "<getProductCompatibilitiesRequest "+\
                "xmlns='http://www.ebay.com/marketplace/marketplacecatalog/v1/services'>"+\
                "<productIdentifier>"+\
                    "<ePID>76715700</ePID>"+\
                "</productIdentifier>"+\
                "<applicationPropertyFilter>"+\
                    "<propertyName>Make</propertyName>"+\
                    "<value>"+\
                        "<text>"+\
                            "<value>Honda</value>"+\
                        "</text>"+\
                    "</value>"+\
                "</applicationPropertyFilter>"+\
                "<sortOrder>"+\
                    "<sortOrder>"+\
                        "<propertyName>Model</propertyName>"+\
                        "<order>Ascending</order>"+\
                    "</sortOrder>"+\
                    "<sortPriority>Sort1</sortPriority>"+\
                "</sortOrder>"+\
                "</getProductCompatibilitiesRequest>"
    
    return requestXml
 
 
# specify the connection to the eBay Sandbox environment
connection = httplib.HTTPSConnection(serverUrl)
 
# specify a POST with the results of generateHeaders and generateRequest
connection.request("POST", serverDir, buildRequestXml(), buildHttpHeaders())
response = connection.getresponse()

# if response was unsuccessful, output message
data = response.read()
connection.close()
response = parseString(data)

print ((response.getElementsByTagName('timestamp')[0]).childNodes[0]).nodeValue
if response.status != 200:
    print "Error sending request:" + response.reason
 
else: #response successful
    # store the response data and close the connection
    print 333333
    data = response.read()
    connection.close()
 
    # parse the response data into a DOM
    response = parseString(data)
    pretty_xml_as_string = response.toprettyxml()
    print pretty_xml_as_string
    # check for any Errors
    errorNodes = response.getElementsByTagName('Errors')
    if (errorNodes != []): #there are errors
        print "<P><B>eBay returned the following errors</B>"
        #Go through each error:
        for error in errorNodes:
            print 123456
            #output the error code and short message
            print "<P>" + ((error.getElementsByTagName('ErrorCode')[0]).childNodes[0]).nodeValue
            print " : " + ((error.getElementsByTagName('ShortMessage')[0]).childNodes[0]).nodeValue.replace("<", "&lt;")
            #output Long Message if it exists (depends on ErrorLevel setting)
            if (error.getElementsByTagName('LongMessage')!= []):
                print "<BR>" + ((error.getElementsByTagName('LongMessage')[0]).childNodes[0]).nodeValue.replace("<", "&lt;")
 
    else: #eBay returned no errors - output results
        # check for the <EBayTime> tag and print
        print 112333333
        if (response.getElementsByTagName('Timestamp')!=[]):
            print "<P><B>Official eBay Time is: "
            #print response
            print ((response.getElementsByTagName('Timestamp')[0]).childNodes[0]).nodeValue, " GMT</B>"
 
 
 
 
    # force garbage collection of the DOM object
    response.unlink()
 
 
#finish HTML page
print "</BODY>"
print "</HTML>"