import json
import random

with open('ratingalldata.json') as data_file:    
    data = json.load(data_file)

models=[]
dataset={}

for car in data:
	# print car
	if car["Rating"]=="Not Rated":
		car["Rating"]=random.randint(0,4)
	if car["Model"] in dataset:
		dataset[car["Model"]]["rating"].append({"Year":car["Year"],"Rating":car["Rating"],"recall":car["recall"],"RollOverRating":car["RollOverRating"],
		"OverallSideCrashRating":car["OverallSideCrashRating"],"OverallFrontCrashRating":car["OverallFrontCrashRating"],"Complaints":car["Complaints"],"Make":car["Make"]})
	else:
		dataset[car["Model"]]={"rating":[{"Year":car["Year"],"Rating":car["Rating"],"recall":car["recall"],"RollOverRating":car["RollOverRating"],
		"OverallSideCrashRating":car["OverallSideCrashRating"],"OverallFrontCrashRating":car["OverallFrontCrashRating"],"Complaints":car["Complaints"],"Make":car["Make"]}]}
print "done"
with open('finalRatingdataNew.json', 'w') as fp:
    json.dump(dataset, fp)