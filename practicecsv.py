# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 22:41:07 2020

@author: SivaSubramaniyaSekar
"""

# this script to read, write data from CSV file
import csv
import pandas as pnd

def csvread_option():
    
    rtype= input('Please enter option -- Read(r) or Write (w)')
    
    if rtype == 'r':
        with open('C:\\Users\\SivaSubramaniyaSekar\\.spyder-py3\\practice\\test.csv','r') as readobj:
            csv_reader=csv.reader(readobj)
            rows=list(csv_reader)
            
            for a in rows:
                print(a)
    
    elif rtype == 'w':
        new_row = []
        col1=input('first value')
        col2=input('Second value')
        col3=input('third value')
        
        new_row.append(col1)
        new_row.append(col2)
        new_row.append(col3)
        
        with open('C:\\Users\\SivaSubramaniyaSekar\\.spyder-py3\\practice\\test.csv', 'a') as appendobj:
            append=csv.writer(appendobj)
            append.writerow(new_row)
            
    else:
        print("Please enter vaild option")