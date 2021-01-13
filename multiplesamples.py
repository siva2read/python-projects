# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 20:49:49 2021

@author: harishs
"""
# to 
# var = input('Please enter string to replace (Vowels - #, newline - |, whitespace - ~)   ')

# print('conversion in progress')

# var1=''

# vow = 'AEIOUaeiou'

# for i in vow:
#     var = var.replace(i,'#')

# var = var.replace(' ','~')
# var = var.replace('\n','|')

# print (var)

# to find count of words in string
# var = input('Please enter string to replace (to count the number of words)   ')


# var = var.lower()

# var = var.split(" ")

# vardict = {}

# wordcount = 0

# for i in var:
#     if i in vardict:
#         vardict[i] += 1
#     else:
#         vardict[i] = 1

# print(vardict)

# # print(var)

# # to have input of student mark and cal percentage
# x = input('No of subjects  ')

# stdmard = {}
# mark=[]
# subject=[]

# tot = 0

# for i in range(int(x)):
#     subject.append(input('enter subject name '))
#     mark.append(input('enter mark '))

# print (mark)
# print (subject)
    
# for j in mark:
#     tot = int(tot)+int(j)

# print(tot)

# percent = int(int(tot)/int(x))

# print('Percentage is  ' + str(percent) + '%')

# stdmard = {subject[i]: mark[i] for i in range(len(mark))}
# print("Dictionary from lists :\n ",stdmard)


life = {
    'animals': {
        'cats': ['Henri', 'Grumpy', 'Lucy'],
        'octopi': '',
        'emus': '',
        },
    'plants': '',
    'other': ''
    }



def print_keys(dic):
    for key, value in dic.items():
        print(key)
        if isinstance(value, dict):
            print_keys(value)
            

print_keys(life)