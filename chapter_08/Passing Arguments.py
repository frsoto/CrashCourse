# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 20:41:23 2021

@author: DELL
"""


def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
# describe_pet('harry', 'hamster')


# # A dog named Willie.
# describe_pet('willie')
# describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')