# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 20:26:33 2021

@author: DELL
"""


def get_formatted_name(first, last, middle=''):
    """Generate a neatly-formatted full name."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()