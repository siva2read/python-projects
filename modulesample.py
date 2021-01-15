# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 19:54:24 2021

@author: harishs
"""

import random

def randomfunc (charlist, cnum):
    
    print ('processing')
    random.shuffle(charlist)
    print(charlist)
   
    print ('processing - int')
    random.randint(0,cnum)
    print(cnum)


# import modulesample as m

# lst = ['A','B','C','D','E','F']

# y = m.randomfunc(lst,19)

# print (y)