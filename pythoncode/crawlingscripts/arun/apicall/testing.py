print "Content-type: text/html"
print

import cgi, os
#import the HTTP, DOM and ConfigParser modules needed
import httplib, ConfigParser
from xml.dom.minidom import parse, parseString


# open config file
config = ConfigParser.ConfigParser()
config.read("/home/aknauhwar/python/apicall/config.ini")

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
siteID = "0"
#verb specifies the name of the call
verb = "GetItem"
#The API level that the application conforms to
compatabilityLevel = "433"

#setup and parse query string
qs = os.environ.get('QUERY_STRING')
if qs:
    q = cgi.parse_qs(qs)



#Setup the HTML Page with name of call as title
print "<HTML>"
print "<HEAD><TITLE>", verb, "</TITLE></HEAD>"
print "<BODY>"
#show form for user to input itemId
print "<FORM action=\"GetItem.py\" method=\"GET\">"
print "<P>Item ID: "
print "<INPUT type=\"text\" name=\"itemID\">"
print "<BR><INPUT type=\"submit\">"
print "</FORM>"



if qs and q.has_key('itemID'):
    #get itemID
    itemID = q['itemID'][0]
    
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
        requestXml = "<?xml version='1.0' encoding='utf-8'?>"+\
                  "<GetItemRequest xmlns=\"urn:ebay:apis:eBLBaseComponents\">"+\
                  "<RequesterCredentials><eBayAuthToken>" + userToken + "</eBayAuthToken></RequesterCredentials>" + \
                  "<ItemID>" + itemID + "</ItemID>"+\
                  "</GetItemRequest>"
        return requestXml


    # specify the connection to the eBay Sandbox environment
    connection = httplib.HTTPSConnection(serverUrl)

    # specify a POST with the results of generateHeaders and generateRequest
    connection.request("POST", serverDir, buildRequestXml(), buildHttpHeaders())
    response = connection.getresponse()

    # if response was unsuccessful, output message
    if response.status != 200:
        print "Error sending request:" + response.reason
        
    else: #response successful
        # store the response data and close the connection
        data = response.read()
        connection.close()
        
        # parse the response data into a DOM
        response = parseString(data)

        # check for any Errors
        errorNodes = response.getElementsByTagName('Errors')
        if (errorNodes != []): #there are errors
            print "<P><B>eBay returned the following errors</B>"
            #Go through each error:
            for error in errorNodes:
                #output the error code and short message (with special characters replaces)
                print "<P>" + ((error.getElementsByTagName('ErrorCode')[0]).childNodes[0]).nodeValue
                print " : " + ((error.getElementsByTagName('ShortMessage')[0]).childNodes[0]).nodeValue.replace("<", "&lt;")
                #output Long Message (with special characters replaces) if it exists (depends on ErrorLevel setting)
                if (error.getElementsByTagName('LongMessage')!= []):
                    print "<BR>" + ((error.getElementsByTagName('LongMessage')[0]).childNodes[0]).nodeValue.replace("<", "&lt;")

        else: #eBay returned no errors - output results
            
            # get the item's details and output them
            print "<P><B>" + ((response.getElementsByTagName('Title')[0]).childNodes[0]).nodeValue + " (" + itemID + ")</B>"
            primaryCategoryNode = response.getElementsByTagName('PrimaryCategory')[0];
            print "<BR>Category: " + ((primaryCategoryNode.getElementsByTagName('CategoryName')[0]).childNodes[0]).nodeValue
            listingDetailsNode = response.getElementsByTagName('ListingDetails')[0];
            print "<BR>Started: " + ((listingDetailsNode.getElementsByTagName('StartTime')[0]).childNodes[0]).nodeValue
            print "<BR>Ends: " + ((listingDetailsNode.getElementsByTagName('EndTime')[0]).childNodes[0]).nodeValue


            # get the item's price/bid details and output them
            sellingStatusNode = response.getElementsByTagName('SellingStatus')[0];
            currency = (sellingStatusNode.getElementsByTagName('CurrentPrice')[0]).getAttribute('currencyID');
            print "<P>Current Price: " + ((sellingStatusNode.getElementsByTagName('CurrentPrice')[0]).childNodes[0]).nodeValue + currency
            print "<BR>Start Price: " + ((response.getElementsByTagName('StartPrice')[0]).childNodes[0]).nodeValue + currency
            print "<BR>BuyItNow Price: " + ((response.getElementsByTagName('BuyItNowPrice')[0]).childNodes[0]).nodeValue + currency
            print "<BR>Bid Count: " + ((sellingStatusNode.getElementsByTagName('BidCount')[0]).childNodes[0]).nodeValue

            #Get and output seller details if there
            seller = response.getElementsByTagName('Seller')
            if (seller!=[]):
                print "<P><B>Seller</B>"
                print "<BR>UserID: " + (((seller[0]).getElementsByTagName('UserID')[0]).childNodes[0]).nodeValue
                print "<BR>Registered: " + (((seller[0]).getElementsByTagName('RegistrationDate')[0]).childNodes[0]).nodeValue
                print "<BR>Feebback Score: " + (((seller[0]).getElementsByTagName('FeedbackScore')[0]).childNodes[0]).nodeValue
