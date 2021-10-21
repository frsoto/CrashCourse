# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 20:12:34 2021

@author: DELL
"""

# =============================================================================
# 6-1: Person
# Use a dictionary to store information about a person you know. Store their 
# first name, last name, age, and the city in which they live. You should have
#  keys such as first_name, last_name, age, and city. Print each piece of 
#  information stored in your dictionary.
# =============================================================================

# person = {
#     'first_name': 'eric',
#     'last_name': 'matthes',
#     'age': 43,
#     'city': 'sitka',
#     }

# print(person['first_name'])
# print(person['last_name'])
# print(person['age'])
# print(person['city'])

# print(person)








# =============================================================================
# 6-2: Favorite Numbers
# Use a dictionary to store people’s favorite numbers. Think of five names, 
# and use them as keys in your dictionary. Think of a favorite number for each 
# person, and store each as a value in your dictionary.Print each person’s name 
# and their favorite number. For even more fun, poll a few friends and get some
# actual data for your program.
# =============================================================================

# favorite_numbers = {
#     'mandy': 42,
#     'micah': 23,
#     'gus': 7,
#     'hank': 1000_000,
#     'maggie': 0,
#     }

# num = favorite_numbers['mandy']
# print(f"Mandy's favorite number is {num}.")

# num = favorite_numbers['micah']
# print(f"Micah's favorite number is {num}.")

# num = favorite_numbers['gus']
# print(f"Gus's favorite number is {num}.")

# num = favorite_numbers['hank']
# print(f"Hank's favorite number is {num}.")

# num = favorite_numbers['maggie']
# print(f"Maggie's favorite number is {num}.")




# =============================================================================
# 6-3: Glossary
# A Python dictionary can be used to model an actual dictionary. However, to 
# avoid confusion, let’s call it a glossary.
# 
# Think of five programming words you’ve learned about in the previous chapters.
# Use these words as the keys in your glossary, and store their meanings as 
#  values.
# Print each word and its meaning as neatly formatted output. You might print
# the word followed by a colon and then its meaning, or print the word on one 
# line and then print its meaning indented on a second line. Use the newline
# character ('\n') to insert a blank line between each word-meaning pair in
# your output.
# =============================================================================
# glossary = {
#     'string': 'A series of characters.',
#     'comment': 'A note in a program that the Python interpreter ignores.',
#     'list': 'A collection of items in a particular order.',
#     'loop': 'Work through a collection of items, one at a time.',
#     'dictionary': "A collection of key-value pairs.",
#     }

# word = 'string'
# print(f"\n{word.title()}: {glossary[word]}")
# word = 'comment'
# print(f"\n{word.title()}: {glossary[word]}")
# word = 'list'
# print(f"\n{word.title()}: {glossary[word]}")
# word = 'loop'
# print(f"\n{word.title()}: {glossary[word]}")
# word = 'dictionary'
# print(f"\n{word.title()}: {glossary[word]}")





# =============================================================================
# 6-4: Glossary 2
# Now that you know how to loop through a dictionary, clean up the code from 
# Exercise 6-3 (page 99) by replacing your series of print statements with a 
# loop that runs through the dictionary’s keys and values. When you’re sure
#  that your loop works, add five more Python terms to your glossary. 
#  When you run your program again, these new words and meanings should 
#  automatically be included in the output.
# =============================================================================

# glossary = {
#     'string': 'A series of characters.',
#     'comment': 'A note in a program that the Python interpreter ignores.',
#     'list': 'A collection of items in a particular order.',
#     'loop': 'Work through a collection of items, one at a time.',
#     'dictionary': "A collection of key-value pairs.",
#     'key': 'The first item in a key-value pair in a dictionary.',
#     'value': 'An item associated with a key in a dictionary.',
#     'conditional test': 'A comparison between two values.',
#     'float': 'A numerical value with a decimal component.',
#     'boolean expression': 'An expression that evaluates to True or False.',
#     }

# for word, definition in glossary.items():
#     print(f"\n{word.title()}: {definition}")





# =============================================================================
# 6-5: Rivers
# Make a dictionary containing three major rivers and the country each river 
# runs through. One key-value pair might be 'nile': 'egypt'.
# 
# Use a loop to print a sentence about each river, such as The Nile runs through
#  Egypt.
# Use a loop to print the name of each river included in the dictionary.
# Use a loop to print the name of each country included in the dictionary.
# =============================================================================

# rivers = {
#     'nile': 'egypt',
#     'mississippi': 'united states',
#     'fraser': 'canada',
#     'kuskokwim': 'alaska',
#     'yangtze': 'china',
#     }

# for river, country in rivers.items():
#     print(f"The {river.title()} flows through {country.title()}.")

# print("\nThe following rivers are included in this data set:")
# for river in rivers.keys():
#     print(f"- {river.title()}")

# print("\nThe following countries are included in this data set:")
# for country in rivers.values():
#     print(f"- {country.title()}")




# =============================================================================
# 6-6: Polling
# Use the code in favorite_languages.py (page 104).
# 
# Make a list of people who should take the favorite languages poll. 
# Include some names that are already in the dictionary and some that are not.
# Loop through the list of people who should take the poll. If they have 
# already taken the poll, print a message thanking them for responding. 
# If they have not yet taken the poll, print a message inviting them to take
#  the poll.
#  
# =============================================================================

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

# print("\n")

# coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']
# for coder in coders:
#     if coder in favorite_languages.keys():
#         print(f"Thank you for taking the poll, {coder.title()}!")
#     else:
#         print(f"{coder.title()}, what's your favorite programming language?")




# =============================================================================
# 6-7: People
# Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three
#  dictionaries in a list called people. Loop through your list of people. 
#  As you loop through the list, print everything you know about each person.
# 
# =============================================================================

# # Make an empty list to store people in.
# people = []

# # Define some people, and add them to the list.
# person = {
#     'first_name': 'eric',
#     'last_name': 'matthes',
#     'age': 46,
#     'city': 'sitka',
#     }
# people.append(person)

# person = {
#     'first_name': 'lemmy',
#     'last_name': 'matthes',
#     'age': 2,
#     'city': 'sitka',
#     }
# people.append(person)

# person = {
#     'first_name': 'willie',
#     'last_name': 'matthes',
#     'age': 11,
#     'city': 'sitka',
#     }
# people.append(person)

# # Display all of the information in the dictionary.
# for person in people:
#     name = f"{person['first_name'].title()} {person['last_name'].title()}"
#     age = person['age']
#     city = person['city'].title()
    
#     print(f"{name}, of {city}, is {age} years old.")




# =============================================================================
# 6-8: Pets
# Make several dictionaries, where the name of each dictionary is the name of a 
# pet. In each dictionary, include the kind of animal and the owner’s name. 
# Store these dictionaries in a list called pets. Next, loop through your list 
# and as you do print everything you know about each pet.
# 
# Note: When I decided to post solutions and wrote complete programs to solve 
# each exercise, I realized this problem was not as well phrased as it should
# have been. It doesn’t really make sense to name each dictionary for the pet
#  it describes; that information should really be included in the dictionary,
#  rather than being used as the name of the dictionary. This solution reflects
#  that approach.
# =============================================================================

# # Make an empty list to store the pets in.
# pets = []

# # Make individual pets, and store each one in the list.
# pet = {
#     'animal type': 'python',
#     'name': 'john',
#     'owner': 'guido',
#     'weight': 43,
#     'eats': 'bugs',
# }
# pets.append(pet)

# pet = {
#     'animal type': 'chicken',
#     'name': 'clarence',
#     'owner': 'tiffany',
#     'weight': 2,
#     'eats': 'seeds',
# }
# pets.append(pet)

# pet = {
#     'animal type': 'dog',
#     'name': 'peso',
#     'owner': 'eric',
#     'weight': 37,
#     'eats': 'shoes',
# }
# pets.append(pet)

# # Display information about each pet.
# for pet in pets:
#     print(f"\nHere's what I know about {pet['name'].title()}:")
#     for key, value in pet.items():
#         print(f"\t{key}: {value}")





# =============================================================================
# 6-9: Favorite Places
# Make a dictionary called favorite_places. Think of three names to use as 
# keys in the dictionary, and store one to three favorite places for each 
# person. To make this exericse a bit more interesting, ask some friends to name
#  a few of their favorite places. Loop through the dictionary, and print each 
#  person’s name and their favorite places.
# =============================================================================

# favorite_places = {
#     'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
#     'erin': ['hawaii', 'iceland'],
#     'willie': ['mt. verstovia', 'the playground', 'new hampshire']
#     }

# for name, places in favorite_places.items():
#     print(f"\n{name.title()} likes the following places:")
#     for place in places:
#         print(f"- {place.title()}")
        
        
        

# =============================================================================
# 6-10: Favorite Numbers
# Modify your program from Exercise 6-2 (page 102) so each person can have more
#  than one favorite number. Then print each person’s name along with their
#  favorite numbers.
# =============================================================================
 
# favorite_numbers = {
#     'mandy': [42, 17],
#     'micah': [42, 39, 56],
#     'gus': [7, 12],
#     }

# for name, numbers in favorite_numbers.items():
#     print(f"\n{name.title()} likes the following numbers:")
#     for number in numbers:
#         print(f"  {number}")




# =============================================================================
# 6-11: Cities
# Make a dictionary called cities. Use the names of three cities as keys in 
# your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and 
# one fact about that city. The keys for each city’s dictionary should be 
# something like country, population, and fact. Print the name of each 
# city and all of the information you have stored about it.
# =============================================================================

cities = {
    'santiago': {
        'country': 'chile',
        'population': 6_310_000,
        'nearby mountains': 'andes',
        },
    'talkeetna': {
        'country': 'united states',
        'population': 876_000_000,
        'nearby mountains': 'alaska range',
        },
    'kathmandu': {
        'country': 'nepal',
        'population': 975_453,
        'nearby mountains': 'himilaya',
        }
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['nearby mountains'].title()

    print(f"\n{city.title()} is in {country}.")
    print(f"  It has a population of about {population}.")
    print(f"  The {mountains} mounats are nearby.")





















































 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 