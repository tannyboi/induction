# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 09:49:16 2020

@author: TANMAY MATHUR
"""
import csv
import pandas as pd
records,attributes=[],[]


#reading csv and printing its pd.DataFrame
with open('sample_csv.csv','r') as sample_csv:
    filereader = csv.reader(sample_csv)
    attributes = next(filereader)
    for line in filereader:
        records.append(line)


print('\nFirst 5 rows are:\n') 


csv_out_table=pd.DataFrame(records[0:5])
csv_out_table.columns=attributes
print(csv_out_table)

#writing into csv
mydict =[{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'}, 
         {'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'}, 
         {'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'}, 
         {'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'}, 
         {'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'}, 
         {'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}]

attributes = ['name', 'branch', 'year', 'cgpa']

with open('sample_csv_writing.csv','w') as sample_csv_w:
    csvwriter = csv.DictWriter(sample_csv_w,fieldnames=attributes)
    csvwriter.writeheader()
    csvwriter.writerows(mydict)
    
    
    
    
    
#writing DF to csc
    
dict2 = [ {'college':'BITS','F/S ratio': 'average','number of enrollments':'good'},
         {'college':'DTU','F/S ratio':'good','number of enrollments':'excellent'},
         {'college':'VIT','F/S ratio':'excellent','number of enrollnents':'good'}]
attributes=['college','F/s ratio','number of enrollments']

dframe = pd.DataFrame(dict2)
dframe.to_csv('newly_created_csv.csv') # newly_created_csv will be created after exec
              
    
    
    
    
    
    
    
    
    
    
    