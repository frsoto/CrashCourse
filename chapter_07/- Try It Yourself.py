# -*- coding: utf-8 -*-
# =============================================================================
# 7-1: Rental Car
# Write a program that asks the user what kind of rental car they would like. 
# Print a message about that car, such as “Let me see if I can find you a 
# Subaru”.
# =============================================================================
# car = input("What kind of car would you like?: ")

# print(f"Let me see if I can find you a {car.title()}.")




# =============================================================================
# 7-2: Restaurant Seating
# Write a program that asks the user how many people are in their dinner group. 
# If the answer is more than eight, print a message saying they’ll have to wait 
# for a table. Otherwise, report that their table is ready.
# =============================================================================

# party_size = input("How many people are in your dinner party tonight? ")
# party_size = int(party_size)

# if party_size > 8:
#     print("I'm sorry, you'll have to wait for a table.")
# else:
#     print("Your table is ready.")




# =============================================================================
# 7-3: Multiples of Ten
# Ask the user for a number, and then report whether the number is a multiple
#  of 10 or not.
# =============================================================================
# number = input("Give me a number, please: ")
# number = int(number)

# if number % 10 == 0:
#     print(f"{number} is a multiple of 10.")
# else:
#     print(f"{number} is not a multiple of 10.")





# =============================================================================
# 7-4: Pizza Toppings
# Write a loop that prompts the user to enter a series of pizza toppings until
#  they enter a quit value. As they enter each topping, print a message saying 
#  you’ll add that topping to their pizza.
# =============================================================================
# prompt = "\nWhat topping would you like on your pizza?"
# prompt += "\nEnter 'quit' when you are finished: "

# while True:
#     topping = input(prompt)
#     if topping != 'quit':
#         print(f"  I'll add {topping} to your pizza.")
#     else:
#         break




# =============================================================================
# 7-5: Movie Tickets
# A movie theater charges different ticket prices depending on a person’s age.
#  If a person is under the age of 3, the ticket is free; if they are between
#  3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. 
#  Write a loop in which you ask users their age, and then tel them the cost of 
#  their movie ticket.
# =============================================================================
# prompt = "How old are you?"
# prompt += "\nEnter 'quit' when you are finished. "

# while True:
#     age = input(prompt)
#     if age == 'quit':
#         break
#     age = int(age)

#     if age < 3:
#         print("  You get in free!")
#     elif age < 13:
#         print("  Your ticket is $10.")
#     else:
#         print("  Your ticket is $15.")




# =============================================================================
# 7-8: Deli
# Make a list called sandwich_orders and fill it with the names of various 
# sandwiches. Then make an empty list called finished_sandwiches. Loop through 
# the list of sandwich orders and print a message for each order, such as I 
# made your tuna sandwich. As each sandwich is made, move it to the list of
#  finished sandwiches. After all the sandwiches have been made, print a message
#  listing each sandwich that was made.
# =============================================================================

# sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
# finished_sandwiches = []

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"I'm working on your {current_sandwich} sandwich.")
#     finished_sandwiches.append(current_sandwich)

# print("\n")
# for sandwich in finished_sandwiches:
#     print(f"I made a {sandwich} sandwich.")




# =============================================================================
# 7-9: No Pastrami
# Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 
# 'pastrami' appears in the list at least three times. Add code near the
#  beginning of your program to print a message saying the deli has run out 
#  of pastrami, and then use a while loop to remove all occurences of 'pastrami'
#  from sandwich_orders. Make sure no pastrami sandwiches end up in 
#  finished_sandiches.
# =============================================================================

# sandwich_orders = [
#     'pastrami', 'veggie', 'grilled cheese', 'pastrami',
#     'turkey', 'roast beef', 'pastrami']
# finished_sandwiches = []

# print("I'm sorry, we're all out of pastrami today.")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# print("\n")
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"I'm working on your {current_sandwich} sandwich.")
#     finished_sandwiches.append(current_sandwich)

# print("\n")
# for sandwich in finished_sandwiches:
#     print(f"I made a {sandwich} sandwich.")




# =============================================================================
# 7-10: Dream Vacation
# Write a program that polls users about their dream vacation. 
# Write a prompt similar to If you could visit one place in the world,
#  where would you go? Include a block of code that prints the results 
#  of the poll.
# =============================================================================

name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

# Responses will be stored in the form {name: place}.
responses = {}

while True:
    # Ask the user where they'd like to go.
    name = input(name_prompt)
    place = input(place_prompt)

    # Store the response.
    responses[name] = place

    # Ask if there's anyone else responding.
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break

# Show results of the survey.
print("\n--- Results ---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")
































