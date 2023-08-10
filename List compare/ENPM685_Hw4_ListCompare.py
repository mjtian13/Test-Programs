# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:21:42 2022

@author: mthak
"""
#name = Munjal Thakkar
#UID = 117530445
#Course: Security Tools
#Section = 0101


#!/usr/bin/python3

import csv

#AD - all sys in AD env - hname,os,build
#EDR - all sys in edr env - hname
#o/p remaining.csv - all sys left to be enrolled in edr
#o/p file shud contain Hostname,Operating System,Build


enrolled_edr = 0
not_enrolled_edr = 0

edr_users = []
not_enrolled_ad_users = []
remaining_count = 0

try:        
    edr_file = open("edr.csv","r")
    edr_reader = csv.reader(edr_file)
    for edr_row in edr_reader:
        edr_users.append(edr_row[0])
except:
    edr_file.close()
    
header = ['Hostname', 'Operating System', 'Build']

try:
    rem_file = open("remaining.csv","w")
    rem_writer = csv.writer(rem_file, lineterminator = '\n')
    rem_writer.writerow(header)

except:
    rem_file.close()
    
try:
    ad_file = open("ad.csv","r")
    ad_reader = csv.reader(ad_file)
    for row in ad_reader:
        if row[0] in edr_users:
            enrolled_edr  += 1
        else:
            not_enrolled_edr +=1
            #rem_writer.writerow(row)
            not_enrolled_ad_users.append(row)
    rem_writer.writerows(not_enrolled_ad_users)
except:
    ad_file.close()
    rem_file.close()
    
ad_file.close()
rem_file.close()
edr_file.close()
        
#print(not_enrolled_ad_users)
print ("Systems remaining to be enrolled in EDR are: " + str(not_enrolled_edr))
print ("Systems enrolles in EDR are: " + str(enrolled_edr - 1))

