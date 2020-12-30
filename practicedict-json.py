# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 17:33:03 2020

@author: SivaSubramaniyaSekar

Dictinory to JSON and Vice versa
"""
import json
#import itertools

mydictobjkey = []
mydictobjvalues = []

mydictobj = {}

num = input('Enter the number of key value pairs')

for i in range(int(num)):
    print(i)
    mydictobjkey.append(input('enter key of dictionary'))
    mydictobjvalues.append(input('enter value of dictionary'))
    print(i)


for key in mydictobjkey:
    for values in mydictobjvalues:
        mydictobj[key] = values
        mydictobjvalues.remove(values)
        break

print('Dictonary Object is %s' % mydictobj)   

        
myjson = json.dumps(mydictobj)
with open ('dictjson.json','w') as f:
    f.write(myjson)
    f.close()


print ('Json file Sucessfully Created')

print('To read json file')

myRecord = json.load(open('dictjson.json'))
print(myRecord)

 

# # converting it to iterable to avoid repetition
# plain_list_iter = iter(mydictobj)

# # converting the plain_list to dict
# plain_list_dict_object = itertools.zip_longest(plain_list_iter, plain_list_iter, fillvalue=None)

# # convert the zip_longest object to dict using `dict`
# plain_list_dict = dict(plain_list_dict_object)

# # print it
# print(plain_list_dict)
