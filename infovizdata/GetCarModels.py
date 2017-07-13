'''
Created on Feb 1, 2017

@author: kkallepalli
'''
import json
import urllib2
import cookielib

modelTypes={}
engine_fuelTypes={}
modelDriveType={}
makeCountry={}
year="2010"

data=[]

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req=urllib2.Request("http://www.carqueryapi.com/api/0.3/?callback=?&cmd=getMakes&year="+year+"&sold_in_us=1",headers=hdr)

page= urllib2.urlopen(req)
resp=str(page.read())
#print resp[1:-1]
content = json.loads(resp[2:-2])

for make in content["Makes"]:
    print "http://www.carqueryapi.com/api/0.3/?callback=?&cmd=getTrims&year="+year+"&make="+make["make_id"]
    req1=urllib2.Request("http://www.carqueryapi.com/api/0.3/?callback=?&cmd=getTrims&year="+year+"&make="+make["make_id"],headers=hdr)

    page1= urllib2.urlopen(req1)
    resp1=str(page1.read())
    #print resp[1:-1]
    content1 = json.loads(resp1[2:-2])
    
    for car in content1["Trims"]:
        data.append(car)
        if car["model_body"] in modelTypes.keys():
            modelTypes[car["model_body"]] +=1
        else:
            modelTypes[car["model_body"]] =1
             
        if car["model_drive"] in modelDriveType.keys():
            modelDriveType[car["model_drive"]] +=1
        else:
            modelDriveType[car["model_drive"]] =1
             
        if car["model_engine_fuel"] in engine_fuelTypes.keys():
            engine_fuelTypes[car["model_engine_fuel"]] +=1
        else:
            engine_fuelTypes[car["model_engine_fuel"]] =1
          
        if car["make_country"] in makeCountry.keys():
            makeCountry[car["make_country"]] +=1
        else: 
            makeCountry[car["make_country"]] =1



print modelTypes
 
print modelDriveType
 
print engine_fuelTypes
 
print makeCountry

print "cars found : "+str(len(data))

with open(year+'alldata.txt', 'w') as outfile:
    json.dump(data, outfile)