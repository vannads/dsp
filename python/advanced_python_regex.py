#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 15:47:20 2017

@author: sathisavannadil
"""
import csv
import re
from collections import Counter


infile = csv.DictReader(open("faculty.csv"))

degrees = []
titles = []
emails = []

for row in infile:
    degrees.append(row[" degree"])
    titles.append(row[" title"])
    emails.append(row[" email"])

#---------------------------------------------
# Q1 : Different degrees and their frequencies
#---------------------------------------------

# Defining degree patterns
pattern1 = r"(?i)\s*Ph\.*\s*D\.*\s*"
pattern2 = r"(?i)\s*B\s*\.*S\s*\.*Ed\s*\.*"
pattern3 = r"(?i)\s*M\s*\.*S\s*\.*"
pattern4 = r"(?i)\s*J\s*\.*D\s*\.*"
pattern5 = r"(?i)\s*M\s*\.*A\s*\.*"
pattern6 = r"(?i)\s*M\s*\.*P\s*\.*H\s*\.*"
pattern7 = r"(?i)\s*S\s*\.*C\s*\.*D\s*\.*"
pattern8 = r"(?i)\s*M\s*\.*D\s*\.*"
    
p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = 0

for degree in degrees:
    if re.search(pattern1, degree):
        p1 += 1
    if re.search(pattern2, degree):
        p2 += 1
    if re.search(pattern3, degree):
        p3 += 1
    if re.search(pattern4, degree):
        p4 += 1  
    if re.search(pattern5, degree):
        p5 += 1 
    if re.search(pattern6, degree):
        p6 += 1 
    if re.search(pattern7, degree):
        p7 += 1 
    if re.search(pattern8, degree):
        p8 += 1 
        
print("Q1")        
print("---------------------") 
print("Degrees : Frequencies") 
print("---------------------")     
print("PhD     :", p1)
print("BS Ed   :", p2)
print("MS      :", p3)
print("JD      :", p4)
print("MA      :", p5)
print("MPH     :", p6)
print("ScD     :", p7)
print("MD      :", p8)
print("======================\n\n")

#---------------------------------------------
# Q2 : Different titles and their frequencies
#---------------------------------------------

# Defining title patterns
pattern10 = r"Assistant\s*Professor"
pattern11 = r"Associate\s*Professor"
pattern12 = r"^Professor"

t1 = t2 = t3 = 0

for title in titles:
    if re.search(pattern10, title):
        t1 += 1
    if re.search(pattern11, title):
        t2 += 1
    if re.search(pattern12, title):
        t3 += 1

print("Q2")
print("---------------------------------") 
print("Title               : Frequencies") 
print("---------------------------------") 
print("Assistant Professor :", t1)
print("Associate Professor :", t2)
print("Professor :", t3)
print("=================================\n\n")

#---------------------------------------------
# Q3 : List of email addresses
#---------------------------------------------

print("Q3")
print("---------------------------------") 
print("Email addresses:") 
print("---------------------------------") 
print(emails)
print("=================================\n\n")


#---------------------------------------------
# Q4 : Different email domains
#---------------------------------------------
domain = []
for email in emails:
    indx = email[re.search('@', email).start()+1:]
    domain.append(indx)


print("Q4")
print("---------------------------------") 
print("Email domains:") 
print("---------------------------------")
print("List of domains:") 
print(list(Counter(domain)))
print("")
print("Domains with frequencies:")
print(dict(Counter(domain)))
print("=================================\n\n")