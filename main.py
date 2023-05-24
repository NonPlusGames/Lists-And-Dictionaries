# Store your five favorite foods in five seperate variables.

first_favorite_food = "Pizza"
# 2
# 3
# 4
# 5

# LISTS
# A list is a data structure that stores a collection of values in a single variable.
# Lists are defined using square brackets [].
# Each item in a list is separated by a comma.
# Lists can contain any Python object, including other lists.

fav_foods = []

# Print the second item in your list.

# CRUD
# Create - How to add a new item to a data structure.
# Read - How to access an item in a data structure.
# Update - How to change or replace an item in a data structure.
# Delete - How to remove an item from a data structure.

# CREATE

# fav_foods.append("Sushi")

# READ

# print(fav_foods[1])

# UPDATE

# fav_foods[1] = "Ice Cream Cake"

# DELETE

# GOOGLEALO

# LAB TIME (List Methods)-----------------------------------------------------------------------

#LIST ITERATION

# print("I sure do love " + fav_foods[0] + "!")
# print("I sure do love " + fav_foods[1] + "!")
# print("I sure do love " + fav_foods[2] + "!")
# print("I sure do love " + fav_foods[3] + "!")
# print("I sure do love " + fav_foods[4] + "!")

# Iterating with Range

# for i in range(0, 5):
#   print("I sure do love " + fav_foods[i] + "!")

# Iterating with a List

# for food in fav_foods:
#   print("I sure do love " + food + "!")

# for food in fav_foods:
#   sentence += food
#   sentence += " and "

# print(sentence)

# Iterating with control flow

# some_numbers = [1, 5, 3, 4, 2, 6, 7, 22, 43, 14, 6, 7, 8]

# count_of_even_numbers = 0
# for number in some_numbers:
#   if number % 2 == 0:
#     print(str(number) + " is even")
#     count_of_even_numbers += 1
#   else:
#     print(str(number) + " is odd")

# print("The list contained " + str(count_of_even_numbers) + " even numbers!")

# LAB TIME (List Iteration) -----------------------------------------------------------------------

# DICTIONARIES
# A dictionary is a data structure that stores a collection of key-value pairs in a single variable.
# Dictionaries are defined using curly braces {}.
# Each key-value pair is separated by a comma.
# Each key is separated from its value by a colon.
# Keys must be unique, but values can be duplicated.

# Ralfy = ["Rafael", "Mota", 32, "Brown", "Black", 6.2, 230, "ralfy@giantmachines.com", "(877)-393-4448"]

# Dictionary version of Ralfy

# Ralfy = {
#   "first_name": "Rafael",
#   "last_name": "Mota",
#   "age": 32,
#   "hair_color": "Brown",
#   "eye_color": "Black",
#   "height": 6.2,
#   "weight": 230,
#   "email": "ralfy@giantmachines",
#   "phone_number": "(877)-393-4448"
# }

# Print just height


# Similarities / Differences between Lists and Dictionaries???


# CRUD for Dictionaries

# CREATE

# Ralfy["favorite_food"] = "Pizza"

# READ

# print(Ralfy["favorite_food"])

# UPDATE

# DELETE

# Dictionary Iteration

# superheroes = {
#   EVERYONES FAVORITE SUPERHEROES
#   "Ralfy": "Spiderman",
# }

# for person in superheroes:
#   print(person + "'s favorite superhero is " + superheroes[person] + ".")