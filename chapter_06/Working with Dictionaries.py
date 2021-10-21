# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 20:13:48 2021

@author: DELL
"""

# alien_0 = {'color': 'green', 'points': 5}
# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")

# alien_0 = {'color': 'green'}
# print(alien_0['color'])


# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)


# alien_0 = {'color': 'green'}
# print(f"The alien is {alien_0['color']}.")
# alien_0['color'] = 'yellow'
# print(f"The alien is now {alien_0['color']}.")


# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print("Original position: " + str(alien_0['x_position']))

# # Move the alien to the right.
# # Figure out how far to move the alien based on its speed.
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     # This must be a fast alien.
#     x_increment = 3

# # The new position is the old position plus the increment.
# alien_0['x_position'] = alien_0['x_position'] + x_increment

# print("New position: " + str(alien_0['x_position']))




# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }

# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " + language.title() + ".")



alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)








































