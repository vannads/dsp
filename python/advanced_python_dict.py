#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 22:11:41 2017

@author: sathisavannadil
"""

import csv
from collections import defaultdict

data_dict = defaultdict(list)

infile = csv.DictReader(open("faculty.csv"))

degrees = []
titles = []
emails = []
names = []
newZip = []

# Part 3 : Q6

for row in infile:
    degrees.append(row[" degree"])
    titles.append(row[" title"])
    emails.append(row[" email"])
    names.append(row["name"].split()[-1])

newZip = (zip(names, zip(degrees, titles, emails)))

faculty_dict = dict()

for item in newZip:
    if item[0] in faculty_dict:
        faculty_dict[item[0]].append(item[1])
    else:
        faculty_dict[item[0]] = [item[1]]
        
for i in faculty_dict:
    print(faculty_dict)  
    
    
# Part 3 : Q7

professor_dict = dict()

for row in infile:
    degrees.append(row[" degree"])
    titles.append(row[" title"])
    emails.append(row[" email"])
    names.append(row["name"].split()[:1] + ','+ row["name"].split()[-1])

for i in names:
    print(i)