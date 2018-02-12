import json

with open('2013alldata.json') as data_file:    
    data = json.load(data_file)
network=[]

for car in data:
	if car["model_sold_in_us"]=="1":
		network.append(car)



with open('2013alldataNew.json', 'w') as fp:
	json.dump(network, fp)
print("done")