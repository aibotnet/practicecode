from subprocess import Popen
import json

testing = "HelloWorld"

jsonStr = '{"script":"#!/bin/bash \\n STRING=\'Hello World\' \\n echo $STRING \\n "}'

j = json.loads(jsonStr)

print "start"
Process=Popen([j ,% (str(23),], shell=True)
#print Process

print "end"