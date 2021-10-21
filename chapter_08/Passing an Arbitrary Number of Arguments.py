# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 20:42:11 2021

@author: DELL
"""

# def make_pizza(size, *toppings):
#     """Summarize the pizza we are about to make."""
#     print("\nMaking a " + str(size) +
#           "-inch pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)
        
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)


# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile

# user_profile = build_profile('albert', 'einstein',
#                              location='princeton',
#                              field='physics')
# print(user_profile)


