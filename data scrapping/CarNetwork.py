import json

network={"nodes":[],"links":[]}
models=[]

with open('2010alldata.json') as data_file:    
    data = json.load(data_file)

for car in data:
	if car["model_name"] not in models:
		if car["model_body"]=="Sedan":
			network["nodes"].append({"name":car["model_name"],"group":car["make_display"],"ttype":car["model_transmission_type"],
				"dtype":car["model_drive"],"country":car["make_country"],"mileage":car["model_lkm_city"],"fuel":car["model_engine_fuel"]})
			models.append(car["model_name"])

for i in range(0,len(network["nodes"])):
	for j in range(i,len(network["nodes"])):
		weight=0
		if network["nodes"][i]["ttype"]==network["nodes"][j]["ttype"]:
			weight +=0
		if network["nodes"][i]["dtype"]==network["nodes"][j]["dtype"]:
			weight +=1
		if network["nodes"][i]["country"]==network["nodes"][j]["country"]:
			weight +=0
		if network["nodes"][i]["mileage"]==network["nodes"][j]["mileage"]:
			weight +=1
		if network["nodes"][i]["fuel"]==network["nodes"][j]["fuel"]:
			weight +=1
		if weight>=3:
			network["links"].append({"source":(i),"target":(j),"weight":weight})

with open('data.json', 'w') as fp:
    json.dump(network, fp)
print("done")