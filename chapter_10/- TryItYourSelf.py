# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 19:25:41 2021

@author: DELL
"""

# =============================================================================
# 10-1: Learning Python
# Open a blank file in your text editor and write a few lines summarizing what
#  you’ve learned about Python so far. Start each line with the phrase In 
#  Python you can… Save the file as learning_python.txt in the same directory
#  as your exercises from this chapter. Write a program that reads the file
#  and prints what you wrote three times. Print the contents once by reading
#  in the entire file, once by looping over the file object, and once by 
#  storing the lines in a list and then working with them outside the 
#  with block.
# learning_python.txt:
# =============================================================================

# filename = 'learning_python.txt'

# print("--- Reading in the entire file:")
# with open(filename) as f:
#     contents = f.read() # el metodo read lee todo el contenido y se guarda como
#                         # string
# with open(filename) as f:
#     contents = f.read() # el metodo read lee todo el contenido y se guarda como
#                         # string
# print(contents)
# print(contents.rstrip())



# print("\n--- Looping over the lines:")
# with open(filename) as f:
#     for line in f:
#         print(line.rstrip())

# print("\n--- Looping over the lines sin rstrip:")
# with open(filename) as f:
#     for line in f:
#         print(line)
        
        
# print("\n--- Storing the lines in a list:")
# with open(filename) as f:
#     lines = f.readlines()
# print(lines)
# for line in lines:
#     print(line.rstrip())
    




# =============================================================================
# 10-2: Learning C
# You can use the replace() method to replace any word in a string with a
#  different word. Here’s a quick example showing how to replace 'dog' with
#  'cat' in a sentence:
    
# >>> message = "I really like dogs."
# >>> message.replace('dog', 'cat')
# 'I really like cats.'

# Read in each line from the file you just created, learning_python.txt, 
# and replace the word Python with the name of another language, such as C.
#  Print each modified line to the screen.
# =============================================================================

# filename = 'learning_python.txt'

# with open(filename) as f:
#     lines = f.readlines()

# for line in lines:
#     # Get rid of newline, then replace Python with C.
#     line = line.rstrip()
#     print(line.replace('Python', 'C'))

# for line in lines:
#     # Get rid of newline, then replace Python with C.
#     print(line.rstrip().replace('Python', 'C'))




# =============================================================================
# 10-3: Guest
# Write a program that prompts the user for their name. When they respond,
#  write their name to a file called guest.txt.
# =============================================================================

# name = input("What's your name? ")

# filename = 'guest.txt'

# with open(filename, 'w') as f:
#     f.write(name)




# =============================================================================
# 10-4: Guest Book
# Write a while loop that prompts users for their name. When they enter
#  their name, print a greeting to the screen and add a line recording 
#  their visit in a file called guest_book.txt. Make sure each entry appears
#  on a new line in the file.
# =============================================================================

# filename = 'guest_book.txt'

# print("Enter 'quit' when you are finished.")
# while True:
#     name = input("\nWhat's your name? ")
#     if name == 'quit':
#         break
#     else:
#         with open(filename, 'a') as f:
#             f.write(f"{name}\n")
#         print(f"Hi {name}, you've been added to the guest book.")



# =============================================================================
# 10-5: Programming Poll
# Write a while loop that asks people why they like programming. 
# Each time someone enters a reason, add their reason to a file that 
# stores all the responses.
# 
# =============================================================================

# filename = 'programming_poll.txt'

# responses = []
# while True:
#     response = input("\nWhy do you like programming? ")
#     responses.append(response)

#     continue_poll = input("Would you like to let someone else respond? (y/n) ")
#     if continue_poll != 'y':
#         break

# with open(filename, 'a') as f:
#     for response in responses:
#         f.write(f"{response}\n")




# =============================================================================
# 10-6: Addition
# One common problem when prompting for numerical input occurs when people 
# provide text instead of numbers. When you try to convert the input to an int,
#  you’ll get a ValueError. Write a program that prompts for two numbers. 
#  Add them together and print the result. Catch the TypeError if either input
#  value is not a number, and print a friendly error message. Test your program
#  by entering two numbers and then by entering some text instead of a number.
# =============================================================================

# x = input("Give me a number: ")
# x = int(x)


# try:
#     x = input("Give me a number: ")
#     x = int(x)

#     y = input("Give me another number: ")
#     y = int(y)
    
# except ValueError:
#     print("Sorry, I really needed a number.")
# else:
#     sum = x + y
#     print(f"The sum of {x} and {y} is {sum}.")






# =============================================================================
# 10-7: Addition Calculator
# Wrap your code from Exercise 10-6 in a while loop so the user can continue
#  entering numbers even if they make a mistake and enter text instead of a
#  number.
# =============================================================================

# print("Enter 'q' at any time to quit.\n")

# while True:
#     try:
#         x = input("\nGive me a number: ")
#         if x == 'q':
#             break

#         x = int(x)

#         y = input("Give me another number: ")
#         if y == 'q':
#             break

#         y = int(y)

#     except ValueError:
#         print("Sorry, I really needed a number.")

#     else:
#         sum = x + y
#         print(f"The sum of {x} and {y} is {sum}.")



# =============================================================================
# 10-8: Cats and Dogs
# Make two files, cats.txt and dogs.txt. Store at least three names of cats
#  in the first file and three names of dogs in the second file. Write a
#  program that tries to read these files and print the contents of the file
#  to the screen. Wrap your code in a try-except block to catch the FileNotFound
#  error, and print a friendly message if a file is missing. Move one of the
#  files to a different location on your system, and make sure the code in the
#  except block executes properly.
# =============================================================================

# filenames = ['cats.txt', 'dogs.txt']

# for filename in filenames:
#     print(f"\nReading file: {filename}")
#     try:
#         with open(filename) as f:
#             contents = f.read()
#             print(contents)
#     except FileNotFoundError:
#         print("  Sorry, I can't find that file.")



# =============================================================================
# 10-9: Silent Cats and Dogs
# Modify your except block in Exercise 10-8 to fail silently if either 
# file is missing.
# =============================================================================

# filenames = ['cats.txt', 'dogs.txt']

# for filename in filenames:
    
#     try:
#         with open(filename) as f:
#             contents = f.read()

#     except FileNotFoundError:
#         pass

#     else:
#         print(f"\nReading file: {filename}")
#         print(contents)



# =============================================================================
# 10-10: Common Words
# Visit Project Gutenberg (https://gutenberg.org/) and find a few texts you’d
#  like to analyze. Download the text files for these works, or copy the raw
#  text from your browser into a text file on your computer.
# 
# You can use the count() method to find out how many times a word or phrase
#  appears in a string. For example, the following code counts the number of
#  times 'row' appers in a string:
    
# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2
# >>> line.lower().count('row')
# 3 

# Notice that converting the string to lowercase using lower() catches 
# all appearances of the word you’re looking for, regardless of how it’s
# formatted.

# Write a program that reads the files you found at Project Gutenberg and 
# determines how many times the word ‘the’ appears in each text.
#  This will be an approximation because it will also count words such 
#  as ‘then’ and ‘tehre’. Try counting ‘the ‘, with a space in the string,
#  and see how much lower your count is.

# common_words.py
# =============================================================================

# def count_common_words(filename, word):
#     """Count how many times word appears in the text."""
#     # Note: This is a really simple approximation, and the number returned
#     #   will be higher than the actual count.
#     try:
#         with open(filename, encoding='utf-8') as f:
#             contents = f.read()
#     except FileNotFoundError:
#         print("file no exist")
#         pass
#     else:
#         word_count = contents.lower().count(word)

#         msg = f"'{word}' appears in {filename} about {word_count} times."
#         print(msg)

# filename = 'alice2.txt'
# count_common_words(filename, 'the')





# =============================================================================
# 10-11: Favorite Number
# Write a program that prompts for the user’s favorite number.
#  Use json.dump() to store this number in a file. Write a separate 
#  program that reads in this value and prints the message,
#  “I know your favorite number! It’s _____.”
# 
# =============================================================================

# import json

# number = input("What's your favorite number? ")

# with open('favorite_number.json', 'w') as f:
#     json.dump(number, f) #esta funcion guarda number en f
#     print("Thanks! I'll remember that.")




# =============================================================================
# 10-12: Favorite Number Remembered
# Combine the two programs from Exercise 10-11 into one file. 
# If the number is already stored, report the favorite number to the user
#  If not, prompt for the user’s favorite number and store it in a file.
#  Run the program twice to see that it works.
# =============================================================================

# import json

# try:
#     with open('favorite_number.json') as f:
#         number = json.load(f)
# except FileNotFoundError:
#     number = input("What's your favorite number? ")
#     with open('favorite_number.json', 'w') as f:
#         json.dump(number, f)
#     print("Thanks, I'll remember that.")
# else:
#     print(f"I know your favorite number! It's {number}.")




# =============================================================================
# 10-13: Verify User
# The final listing for remember_me.py assumes either that the user has already
#  entered their username or that the program is running for the first time.
#  We should modify it in case the current user is not the person who last 
#  used the program.
# 
# Before printing a welcome back message in greet_user(), ask the user if this
#  is the correct username. If it’s not, call get_new_username() to get the 
#  correct username.
# 
# =============================================================================

# import json

# def get_stored_username():
#     """Get stored username if available."""
#     filename = 'username.json'
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj)
#     except FileNotFoundError:
#         return None
#     else:
#         return username

# def get_new_username():
#     """Prompt for a new username."""
#     username = input("What is your name? ")
#     filename = 'username.json'
#     with open(filename, 'w') as f_obj:
#         json.dump(username, f_obj)
#     return username

# def greet_user():
#     """Greet the user by name."""
#     username = get_stored_username()
#     if username:
#         correct = input(f"Are you {username}? (y/n) ")
#         if correct == 'y':
#             print(f"Welcome back, {username}!")
#         else:
#             username = get_new_username()
#             print(f"We'll remember you when you come back, {username}!")
#     else:
#         username = get_new_username()
#         print(f"We'll remember you when you come back, {username}!")


# greet_user()


# =============================================================================
# You might notice the identical else blocks in this version of greet_user().
#  One way to clean this function up is to use an empty return statement. 
#  An empty return statement tells Python to leave the function without 
#  running any more code in the function.
# Here’s a cleaner version of greet_user():
# =============================================================================

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
        correct = input(f"Are you {username}? (y/n) ")
        if correct == 'y':
            print(f"Welcome back, {username}!")
            return

    # We got a username, but it's not correct.
    # Let's prompt for a new username.
    username = get_new_username()
    print(f"We'll remember you when you come back, {username}!")


greet_user()







    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    