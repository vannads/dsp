#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 16:22:57 2017

@author: sathisavannadil
"""

import csv

#Prepare email list. 
infile = csv.DictReader(open("faculty.csv"))
emails = []

for row in infile:
    emails.append(row[" email"])

#Write emails in file *emails.csv* in the working directory.
with open("emails.csv", "w") as outfile:
    for email in emails:
        outfile.write(email)
        outfile.write('\n')

