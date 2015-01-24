#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("C:\\Users\\Victor\\Desktop\\Udacity\\introml\\ud421-projects\\final_project\\final_project_dataset.pkl", "r"))

#print len(enron_data)

#print enron_data.keys()
#print enron_data['SKILLING JEFFREY K']['total_payments']
#print enron_data['LAY KENNETH L']['total_payments']
#print enron_data['FASTOW ANDREW S']['total_payments']


print enron_data['GLISAN JR BEN F']
#print len(enron_data['GLISAN JR BEN F'])

#email_count = 0
#num_sal_count = 0
#tot_payments_count = 0
#poi_count = 0
#poi_NaN_count = 0
#for key in enron_data:
#    if enron_data[key]['poi']:
#        poi_count+=1
#    if (enron_data[key]['poi'] and enron_data[key]['total_payments'] == 'NaN'):
#        poi_NaN_count+=1
#    if enron_data[key]['total_payments'] == 'NaN':
#        tot_payments_count+=1
##    if enron_data[key]['email_address'] != 'NaN':
##        email_count+=1
##    if enron_data[key]['salary'] != 'NaN':
##        num_sal_count+=1
##        
#print tot_payments_count
##print email_count
##print num_sal_count
#print poi_NaN_count
#print poi_count