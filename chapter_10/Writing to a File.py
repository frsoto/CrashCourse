# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 17:58:27 2021

@author: DELL
"""

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
