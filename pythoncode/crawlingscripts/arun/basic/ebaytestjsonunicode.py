import urllib2
import lxml.html as lh
from bs4 import BeautifulSoup as BS
import requests
import json
import simplejson
import urllib
from json import JSONDecoder
line ='{"noCompatibilityBySpec":false,"status":{"id":1,"name":"SUCCESS"},"hsnTsnExpansion":false,"propertyNames":["FitmentComments","Year","Make","Model","Trim","Engine"],"propertyTypes":[2,2,2,2,2,2],"displayNames":["Notes","Year","Make","Model","Trim","Engine"],"data":[{"FitmentComments":["Part Type: Disc Brake Rotor, Position: Front, Drive Type: 4WD"],"Model":["K5 Blazer"],"Year":["1981"],"Make":["Chevrolet"]},{"FitmentComments":["Part Type: Disc Brake Rotor, Position: Front, Drive Type: 4WD"],"Model":["Jimmy"],"Year":["1981"],"Make":["GMC"]},{"FitmentComments":["Part Type: Disc Brake Rotor, Position: Front"],"Model":["K1500"],"Year":["1981"],"Make":["GMC"]},{"FitmentComments":["Part Type: Disc Brake Rotor, Position: Front"],"Model":["K1500 Suburban"],"Year":["1981"],"Make":["GMC"]},{"FitmentComments":["Part Type: Disc Brake Rotor, Position: Front"],"Model":["Cherokee"],"Year":["1981"],"Make":["Jeep"]},{"FitmentComments":["Part Type: Disc Brake Rotor, Position: Front"],"Model":["J10"],"Year":["1981"],"Make":["Jeep"]},{"FitmentComments":["Part Type: Disc Brake Rotor, Position: Front, Except Splined Drive Hub"],"Model":["Wagoneer"],"Year":["1981"],"Make":["Jeep"]},{"FitmentComments":["Part Type: Disc Brake Rotor, Position: Front"],"Model":["K10"],"Year":["1980"],"Make":["Chevrolet"]},{"FitmentComments":["Part Type: Disc Brake Rotor, Position: Front"],"Model":["K10 Suburban"],"Year":["1980"],"Make":["Chevrolet"]},{"FitmentComments":["Part Type: Disc Brake Rotor, Position: Front, Drive Type: 4WD"],"Model":["K5 Blazer"],"Year":["1980"],"Make":["Chevrolet"]},{"FitmentComments":["Part Type: Disc Brake Rotor, Position: Front, Drive Type: 4WD"],"Model":["Jimmy"],"Year":["1980"],"Make":["GMC"]},{"FitmentComments":["Part Type: Disc Brake Rotor, Position: Front"],"Model":["K1500"],"Year":["1980"],"Make":["GMC"]},{"FitmentComments":["Part Type: Disc Brake Rotor, Position: Front"],"Model":["K1500 Suburban"],"Year":["1980"],"Make":["GMC"]},{"FitmentComments":["Part Type: Disc Brake Rotor, Position: Front, 7/8" Drive Flange"],"Model":["Cherokee"],"Year":["1980"],"Make":["Jeep"]},{"FitmentComments":["Part Type: Disc Brake Rotor, Position: Front, 6 Stud Rotors, Steering Drive Flange"],"Model":["CJ5"],"Year":["1980"],"Make":["Jeep"]},{"FitmentComments":["Part Type: Disc Brake Rotor, Position: Front, Steering Drive Flange, 6 Stud Rotors"],"Model":["CJ7"],"Year":["1980"],"Make":["Jeep"]},{"FitmentComments":["Part Type: Disc Brake Rotor, Position: Front, 7/8" Drive Flange"],"Model":["J10"],"Year":["1980"],"Make":["Jeep"]},{"FitmentComments":["Part Type: Disc Brake Rotor, Position: Front, 7/8" Drive Flange"],"Model":["Wagoneer"],"Year":["1980"],"Make":["Jeep"]},{"FitmentComments":["Part Type: Disc Brake Rotor, Position: Front"],"Model":["K10"],"Year":["1979"],"Make":["Chevrolet"]},{"FitmentComments":["Part Type: Disc Brake Rotor, Position: Front"],"Model":["K10 Suburban"],"Year":["1979"],"Make":["Chevrolet"]}],"errors":[],"uniqueVehicle":false,"fitsDiag":[],"pageInfo":{"currentPageNo":5,"totalRecordCount":176,"totalPageCount":9,"pageRecordCount":20}}'

decoder = JSONDecoder()
s_len = len(line)

objs = []
end = 0
while end != s_len:
        obj, end = decoder.raw_decode(line, idx=end)
        objs.append(obj)


print objs

print "JSON parsing example: ", objs[0]['data'][0]['Model']
