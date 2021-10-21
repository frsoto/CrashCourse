# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 17:58:19 2021

@author: DELL
"""

# filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     lines = file_object.readlines()
    
# print(lines)

# for line in lines:
#     print(line.rstrip())





filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

# print (lines)

pi_string = ''
for line in lines:
    pi_string += line.rstrip()
    
# print(f"{pi_string[-10:]}...")
# print(f"{pi_string[:10]}...")
# print (pi_string)



# birthday = input("Enter your birthday, in the form mmddyy: ")
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")
    















































   
    
    
    
    
    
    
    
    
    
