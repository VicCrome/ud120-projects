#!/usr/bin/python

import pickle
import sys
import re
import os

sys.path.append( "C:\\Users\\Victor\\Desktop\\Udacity\\introml\\ud421-projects\\tools" )
from parse_out_email_text import parseOutText

#"""
#    starter code to process the emails from Sara and Chris to extract
#    the features and get the documents ready for classification
#
#    the list of all the emails from Sara are in the from_sara list
#    likewise for emails from Chris (from_chris)
#
#    the actual documents are in the Enron email dataset, which
#    you downloaded/unpacked in Part 0 of the first mini-project
#
#    the data is stored in lists and packed away in pickle files at the end
#
#"""
#
#
#from_sara  = open("C:\\Users\\Victor\\Desktop\\Udacity\\introml\\ud421-projects\\text_learning\\from_sara.txt", "r")
#from_chris = open("C:\\Users\\Victor\\Desktop\\Udacity\\introml\\ud421-projects\\text_learning\\from_chris.txt", "r")
#
#from_data = []
#word_data = []
#
#### temp_counter is a way to speed up the development--there are
#### thousands of emails from Sara and Chris, so running over all of them
#### can take a long time
#### temp_counter helps you only look at the first 200 emails in the list
#temp_counter = 0
#
#
#for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
#    for path in from_person:
#        ### only look at first 200 emails when developing
#        ### once everything is working, remove this line to run over full dataset
#        temp_counter += 1
#        if temp_counter >= 0:
#            path = os.path.join('C:\\Users\\Victor\\Desktop\\Udacity\\introml\\ud421-projects', path[:-1]).replace("/","\\")
#            print path
#            email = open(path, "r")
#
#            ### use parseOutText to extract the text from the opened email
#            email_reader = parseOutText(email)
#
#            ### use str.replace() to remove any instances of the words
#            ### ["sara", "shackleton", "chris", "germani"]
#            for remove_instances in ["sara", "shackleton", "chris", "germani"]:
#                email_reader.replace(remove_instances,'')
#
#            ### append the text to word_data
#            word_data.append(email_reader)
#
#            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
#            if name == 'sara':
#                from_data.append(0)
#            if name == 'chris':
#                from_data.append(1)
#
#            email.close()
#
#print "emails processed"
#print word_data[152]
#from_sara.close()
#from_chris.close()
#
#pickle.dump( word_data, open("C:\\Users\\Victor\\Desktop\\Udacity\\introml\\ud421-projects\\text_learning\\your_word_data.pkl", "w") )
#pickle.dump( from_data, open("C:\\Users\\Victor\\Desktop\\Udacity\\introml\\ud421-projects\\text_learning\\your_email_authors.pkl", "w") )



word_data = pickle.load( open("C:\\Users\\Victor\\Desktop\\Udacity\\introml\\ud421-projects\\text_learning\\your_word_data.pkl", "r"))

print word_data

### in Part 4, do TfIdf vectorization here
from sklearn.feature_extraction.text import TfidfVectorizer


from nltk.corpus import stopwords

sw = stopwords.words('english')

vectorizer = TfidfVectorizer(stop_words='english',lowercase=True)
word_data_vector = vectorizer.fit_transform(word_data)
#print word_data_vector
print len(vectorizer.get_feature_names())

print vectorizer.get_feature_names()[34596]