#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 3 (decision tree) mini-project

    use an DT to identify emails from the Enron corpus by their authors
    
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time
sys.path.append("C:\\Users\\Victor\\Desktop\\Udacity\\introml\\ud421-projects\\tools")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()



#########################################################
from sklearn import tree
clf = tree.DecisionTreeClassifier(min_samples_split=40)
clf = clf.fit(features_train, labels_train)

acc_min_samples_split_40 = clf.score(features_test, labels_test) 

print "Accuracy is: ", acc_min_samples_split_40
    

print "Number of features is: ", features_train.shape[1]

#########################################################


