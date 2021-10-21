# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 17:58:35 2021

@author: DELL
"""

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")
    
    
    
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")

# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
#     else:
#         print(answer)









# filename = 'alice2.txt'

# try:
#     with open(filename, encoding='utf-8') as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError as e:
#     msg = "Sorry, the file " + filename + " does not exist."
#     print(msg)
# else:
#     # Count the approximate number of words in the file.
#     words = contents.split() #convierte en lista al string
#     num_words = len(words)
#     print("The file " + filename + " has about " + str(num_words) + " words.")






def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f_obj:
            contents = f_obj.read() 
    except FileNotFoundError:
       print(f"Sorry, the file {filename} does not exist.")
    else:
        # Count approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice2.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)































