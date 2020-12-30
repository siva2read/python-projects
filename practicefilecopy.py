# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 18:10:55 2020

@author: SivaSubramaniyaSekar

To move file from one directory to other directory
"""

import shutil

source = 'C:\\Users\\SivaSubramaniyaSekar\\.spyder-py3\\practice\\directory1'

destination = 'C:\\Users\\SivaSubramaniyaSekar\\.spyder-py3\\practice\\directory2'

#dest = shutil.move(source, destination)

dest = shutil.move(source, destination,copy_function=shutil.copytree)

