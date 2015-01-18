#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("C:\\Users\\Victor\\Desktop\\Udacity\\introml\\ud421-projects\\tools")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("C:\\Users\\Victor\\Desktop\\Udacity\\introml\\ud421-projects\\final_project\\final_project_dataset.pkl", "r") )
data_dict.pop('TOTAL',0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

import heapq
print max(data[:,0])
top4 = heapq.nlargest(4,data[:,0])
print top4

for key in data_dict:
    for large_value in top4:
        if data_dict[key]['salary'] == large_value:
            print key

