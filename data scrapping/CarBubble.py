import json

models={}
dataset=[]
model_name={}


with open('2010alldata.json') as data_file:    
    data = json.load(data_file)

for car in data:
	if car["model_body"] not in models.keys():
		models[car["model_body"]]=1
	else:
		if car["model_name"] not in model_name.keys():
			model_name[car["model_name"]]=1
			models[car["model_body"]] +=1


for key in models.keys():
	value=models[key]
	if key==None:
		key="other"
	dataset.append({"model_body":key,"count":value})

with open('2010Bubbledata.json', 'w') as fp:
    json.dump(dataset, fp)
