# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 21:11:07 2021

@author: harishs
"""

import re

f = open('pytst.txt','r')

contents = f.read()
mcontent = contents[9:]

# to update lower case
mcontent = mcontent.lower()

print (mcontent)

# to update number
if (re.findall(r'\d',mcontent)):
    mcontent = re.sub(r'\d','',mcontent)

print (mcontent)

# to update special character
mcontent = re.sub(r'[^#]\W','',mcontent)

print (mcontent)

j = open('pytst.txt','w')

finalcontent = contents[0:8] + mcontent

print(finalcontent)

j.write(finalcontent)
j.close()

# #regex to check username - no digits, uppercase, special characters except #

# #\s, \b, \w+, \D

# x = re.findall(r'[A-Z]|\d|\W',contents)
# #y = re.findall(r'\d',contents)



# y = re.sub('[A-Z]','[a-z}',contents)
# print(y)

# #print(x)
# #print(y)