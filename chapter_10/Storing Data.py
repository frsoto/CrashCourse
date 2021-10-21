# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 17:58:44 2021

@author: DELL
"""
# import json

# numbers = [2, 3, 5, 7, 11, 13]

# filename = 'numbers.json'
# with open(filename, 'w') as file_object:
#     json.dump(numbers, file_object)



# import json

# filename = 'numbers.json'
# with open(filename) as file_object:
#     numbers = json.load(file_object)
    
# print(numbers)








import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()