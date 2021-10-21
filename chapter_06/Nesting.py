# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 20:14:06 2021

@author: DELL
"""

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)





aliens = []

# Make 30 green aliens.
for alien_number in range (0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    
# for alien in aliens:
#     print(alien)  

# Show the first 5 aliens:
# for alien in aliens[0:5]:
#     print(alien)
# print("...")

# print(f"Total number of aliens: {len(aliens)}")

# for alien in aliens[0:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
# # # Show the first 5 aliens.
# # for alien in aliens[:5]:
# #     print(alien)
# #     print("...")

#     elif alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['speed'] = 'fast'
#         alien['points'] = 15




# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
#     }

# # Summarize the order.
# print("You ordered a " + pizza['crust'] + "-crust pizza " +
#       "with the following toppings:")

# for topping in pizza['toppings']:
#     print("\t" + topping)








# favorite_languages = {
# 'jen': ['python', 'ruby'],
# 'sarah': ['c'],
# 'edward': ['ruby', 'go'],
# 'phil': ['python', 'haskell'],
# }

# for name, languages in favorite_languages.items():
#     print(f"\n{name.title()}'s favorite languages are:")
#     for language in languages:
#         print(f"\t{language.title()}")









users = {'aeinstein': {'first': 'albert',
                       'last': 'einstein',
                       'location': 'princeton'},
         'mcurie': {'first': 'marie',
                    'last': 'curie',
                    'location': 'paris'},
         }


for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())



















