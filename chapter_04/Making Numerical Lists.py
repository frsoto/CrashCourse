# -*- coding: utf-8 -*-
# for value in range(1, 5):
#     print(value)
    
# numbers = list(range(1, 6))
# print(numbers)

# even_numbers = list(range(2, 11, 2))
# print(even_numbers)


# squares = []
# squares2 = []
# for value in range(1,11):
#     square = value**2
#     squares.append(square)
#     squares2.append(value**2)
    
# print(squares)
# print(squares2)


squares = [value**2 for value in range(1, 11)]
print(squares)
