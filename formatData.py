import json



with open('2014alldata.json') as data_file:    
    data = json.load(data_file)

for car in data:
	if car["model_body"] =="Standard Pickup Trucks":
		car["model_body"]="Truck"
	else if car["model_body"] =="Sport Utility Vehicles":
		car["model_body"]="SUV"
	else if car["model_body"] =="Midsize Station Wagons":
		car["model_body"]="Station Wagon"
	else if car["model_body"] =="Small Station Wagons":
		car["model_body"]="Station Wagon"
	else if car["model_body"] =="Passenger Vans":
		car["model_body"]="Van"
	else if car["model_body"] =="Not Available":
		car["model_body"]="Other"
	else if car["model_body"] =="Midsize Cars":
		car["model_body"]="Other"
	else if car["model_body"] =="Compact Cars":
		car["model_body"]="Hatchback"



with open('2014Bubbledata.json', 'w') as fp:
    json.dump(data, fp)
