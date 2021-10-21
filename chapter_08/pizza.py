# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 21:12:37 2021

@author: DELL
"""

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")