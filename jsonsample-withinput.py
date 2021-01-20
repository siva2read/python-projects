# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 20:00:25 2021

@author: harishs
"""

import json
import os
import xmltodict

def empdetails():
    
    data = {}
    data['employee details'] = []
    
    empid = input('Enter the EMP ID -->')
    fname = input('Enter the EMP first Name -->')
    lname = input('Enter the EMP last Name -->')
    sal = input('Enter the EMP Salary -->')
    dob = input('Enter the EMP DOB -->')
    doj = input('Enter the EMP DOJ -->')
    pjname = input('Enter the project name -->')

    data['employee details'].append({'emp id': empid})
    data['employee details'].append({'first name': fname})
    data['employee details'].append({'last Name': lname})
    data['employee details'].append({'Salary': sal})
    data['employee details'].append({'DOB': dob})
    data['employee details'].append({'DOJ': doj})
    data['employee details'].append({'project jname': pjname})
    
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)

def xmltojson():
    
    for filename in os.listdir('C:\\Users\\harishs\\.spyder-py3\\practice'):
        if not filename.endswith('.xml'): continue
        fullname = os.path.join('C:\\Users\\harishs\\.spyder-py3\\practice', filename)
        with open(fullname, 'r') as f:
            xmlString = f.read()
        jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)
        with open(fullname, 'w') as x:
            x.write(jsonString)
        
        
        

#empdetails()
xmltojson()