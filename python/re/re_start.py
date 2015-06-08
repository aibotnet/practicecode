import re
import urllib2

def test1():
    str = 'anword:123 example word:ca6!!'
    match = re.search(r'word:\w\w\w ', str)
    # If-statement after search() tests if it succeeded
    if match:
        print 'found', match.group() ## 'found word:cat'
    else:
        print 'did not find'

def test2():
     match = re.search(r'iii', 'piiig')
     if match:
        print 'found', match.group() ## 'found word:cat'
     else:
        print 'did not find'
     match = re.search(r'igs', 'piiig')
     if match:
        print 'found', match.group() ## 'found word:cat'
     else:
        print 'did not find'
     match = re.search(r'..g', 'ddg')
     if match:
        print 'found', match.group() ## 'found word:cat'
     else:
        print 'did not find'


def test3():
    string = 'a55'
    find = re.search(r'(a-z)', string, re.DOTALL)
    print find



def zero_one_more():
    print re.match(r'(bac)+d', 'bacbacd',  re.DOTALL).group()

    match = re.search(r'\d\s*\d\s*\d', 'xx12   3xx')
    print match.group()
    match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx')
    match = re.search(r'\d\s*\d\s*\d', 'xx123xx')


def email():
    string = 'his email id id abc-xyz.pqr@yahoo and my email id is v.i.k.a.s@yahoo.co.in'
    #match = re.search(r'[\w.-]*@[\w.-]+', string)
    #print match.group()
    print re.findall(r'[\w.-]+@[\w-]+[.][\w.-]+', string)

    #print re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@google.com', string)



def extractingLink():
    string = ''

def findAll():
    #doc_string = urllib2.urlopen('http://www.amazon.com/gp/product/B00EOE0WKQ/').read()

    fp = open('test1.txt')
    lol = fp.readlines()
    string = ''
    for l in lol:
        string += l

    #print re.findall(r'mydjangoapp', string, re.DOTALL)

    print re.search(r'^mydjangoapp', string)
    print re.search(r'$mydjangoapp', string)
    print re.search(r'mydjangoapp^', string)
    print re.search(r'mydjangoapp$', string)

    print re.search(r'.*', string).group() # matches one line [whole line]

def main():
    #test1()
    #test2()
    test3()
    #zero_one_more()
    #email()
    #extractingLink()
    #findAll()
main()