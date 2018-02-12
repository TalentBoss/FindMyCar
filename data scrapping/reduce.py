import json

data={}
with open("finalRatingdataNew.json") as json_data:
	data = json.load(json_data)
	for item in data.keys():
		# print item,data[item]["rating"]
		length = len(data[item]["rating"])
		arr={}
		print length
		i=0
		while i<length:
			print data[item]["rating"][i]["Year"]
			if data[item]["rating"][i]["Year"] not in arr.keys():
				arr[data[item]["rating"][i]["Year"]]=[data[item]["rating"][i]["Make"]]
			else:
				if data[item]["rating"][i]["Make"] not in arr[data[item]["rating"][i]["Year"]]:
					arr[data[item]["rating"][i]["Year"]].append(data[item]["rating"][i]["Make"])
				else:
					del(data[item]["rating"][i])
					length = length-1
					i-=1
			i+=1



with open('reduced.json', 'w') as outfile:
    json.dump(data, outfile)

