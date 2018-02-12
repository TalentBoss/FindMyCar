import json



def fun(str1,data):
	network={"nodes":[],"links":[]}
	models=[]
	for car in data:
		if car["model_sold_in_us"].strip(' \t\n\r')=="1":
			if car["model_name"] not in models:
				if car["model_body"]==str1:
					network["nodes"].append({"name":car["model_name"],"group":car["make_display"],"ttype":car["model_transmission_type"],
						"dtype":car["model_drive"],"country":car["make_country"],"mileage":car["model_lkm_city"],"fuel":car["model_engine_fuel"],"cc":car["model_engine_cc"],
						"rpm":car["model_engine_power_rpm"],"doors":car["model_doors"],"cylinders":car["model_engine_cyl"],"engineposition":car["model_engine_position"],
						"enginepower":car["model_engine_power_ps"],"torguqnm":car["model_engine_torque_nm"],"torquerpm":car["model_engine_torque_rpm"],"enginetype":car["model_engine_type"],
						"enginevalves":car["model_engine_valves_per_cyl"],"height":car["model_height_mm"],"length":car["model_length_mm"],"hwymileage":car["model_lkm_hwy"],
						"width":car["model_width_mm"],"wheelbase":car["model_wheelbase_mm"],"weight":car["model_weight_kg"],"modeltrim":car["model_trim"]})
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
			if network["nodes"][i]["width"]==network["nodes"][j]["width"]:
				weight +=1
			if network["nodes"][i]["height"]==network["nodes"][j]["height"]:
				weight +=1
			if network["nodes"][i]["enginepower"]==network["nodes"][j]["enginepower"]:
				weight +=1
			if network["nodes"][i]["enginevalves"]==network["nodes"][j]["enginevalves"]:
				weight +=1
			if network["nodes"][i]["weight"]==network["nodes"][j]["weight"]:
				weight +=1
			if network["nodes"][i]["rpm"]==network["nodes"][j]["rpm"]:
				weight +=1
			if network["nodes"][i]["hwymileage"]==network["nodes"][j]["hwymileage"]:
				weight +=1
			if weight>=4:
				network["links"].append({"source":(i),"target":(j),"weight":weight})

	with open('2014data'+str1+'.json', 'w') as fp:
	    json.dump(network, fp)
	print("done")
	return;


with open('2014Bubbledata.json') as data_fileBubble:    
    dataset = json.load(data_fileBubble)

with open('2014alldataNew.json') as data_file:    
    data = json.load(data_file)

for model in dataset:
	fun(model["model_body"],data)
	print model["model_body"]