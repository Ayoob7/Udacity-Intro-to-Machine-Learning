#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import difflib
from difflib import get_close_matches
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#print type(enron_data)  data[person_name]["poi"]==1
#print len(enron_data['METTS MARK'])
'''count = 0
for person in enron_data:
    if enron_data[person]["poi"] == True:
        count += 1
print count'''

#for eleme in enron_data:
    #print eleme
#salary email_address
count = 0
for eleme in enron_data:
    if enron_data[eleme]['email_address'] != "NaN":
        count += 1
print count


