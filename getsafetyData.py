import json
import urllib2
import cookielib



hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

data={"safety":[]}
safety=[]

f=open("vechileid.txt","rb")
# temp = [line for line in f]
# print temp
for line in f:
	line = line.rstrip('\r\n')
	print line
	vid=line
	url1="https://webapi.nhtsa.gov/api/SafetyRatings/VehicleId/"+vid+"?format=json"
	# print url1
	req1=urllib2.Request(url1,headers=hdr)
	page1=urllib2.urlopen(req1)
	resp1=str(page1.read())
	# print resp1
	content1=json.loads(resp1) 

	for rating in content1["Results"]:
		safety.append({"id":rating["VehicleId"],"Model":rating["Model"],"Make":rating["Make"],"Year":rating["ModelYear"],"recall":rating["RecallsCount"],
			"Complaints":rating["ComplaintsCount"],"RollOverRating":rating["RolloverRating"],"OverallFrontCrashRating":rating["OverallFrontCrashRating"],
			"OverallSideCrashRating":rating["OverallSideCrashRating"],"Rating":rating["OverallRating"]})

	

with open('ratingalldata.json', 'w') as outfile:
    json.dump(safety, outfile)	