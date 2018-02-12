import json

data={}
countries={}
finaldata=[]
with open("names.json") as json_data:
	data = json.load(json_data)
with open("slim-3.json") as json_data:
	countries = json.load(json_data)

for country in data:
	for newCountry in countries["rows"]:
		# print newCountry["name"]
		dict={}
		if country["country"].upper()==newCountry["name"].upper():
			dict=country
			dict["country_code"]=newCountry["country-code"]
			dict["alpha"]=newCountry["alpha-3"]
			finaldata.append(dict)
			print country["country"]


with open('newCountryData.json', 'w') as outfile:
    json.dump(finaldata, outfile)
