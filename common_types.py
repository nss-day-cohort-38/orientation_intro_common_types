# Data Types

# Declare a variable
# sum = 2 + 2
# print(sum)

# Comparisons use double equal
# print(sum != 4)

# ========================================

# Variables adhere to scope, kind of like let in JS...
# name = "Fred"

# def say_name():
# #   ...unless you use 'global'
#     global name
#     name = "Bubba"
#     print("internal", name)

# say_name()
# print("external", name)

# ========================================

# Conditional statement
# name = "Joe"

# if name == "Steve":
#     print("I feel great")
# elif name == "Joe":
#     print("You got the better instructor")
# else:
#     print("I have a cold")

# ========================================

# String concatenation
# print(f"My name is {name}")
# Still have dynamic typing ( but no implicit coercion!)
# Can't do this:
# print(2 + "2")

# ========================================

# *****Collections***** (List, Dictionary, Tuple, Set)

# Lists (ordered, mutable & allows duplicates)

junk = ["Fred", True, [1, 2, 3], 234]

# junk.append(234)
# junk.insert(0, "oh, I get it")
# print(junk[3])
# junk.extend(["Mary", "Joseph", "Bob"])
# print(junk)

# Negative indexing
# junk[-1] = "The last item"
# print(junk)
# print(junk[-4])
# print(junk[0])

# Loop through the items in a list
# for taco in junk:
#     print(taco)

# Javascript equivalent: junk.forEach(taco => console.log(taco));

# You can declare an empty list:
# stuff = []

# Create a NEW list from a subset of values in another list with slice
# my_list = [1, 2, 4, "hello", "monkey"]
# my_subset = my_list[0:3]
# my_subset = my_list[1:3]
# my_subset = my_list[:3]
# my_subset = my_list[2:]
# my_subset = my_list[2:34]
# my_subset = my_list[::2]
# print(my_subset)
# print(my_list)

# ========================================

# Dictionaries (unordered, mutable, does NOT allow duplicates & indexed w/ key value pairs)

# my_pairs = {
#     123: "number",
#     "name": "Broomhilda",
# }

# print(my_pairs["name"])

# Add new properties
# my_pairs["name"] = "Jones"
# my_pairs["address"] = {"number": 123, "street": "Sesame St"}
# print(my_pairs)

# Loop over keys and values
# for key in my_pairs:
#     print(key, my_pairs[key])
#     if True:
#         print("Hello")

# Access different parts of the dict
# print(my_pairs.keys())

# my_pairs_values = my_pairs.values()
# print(type(my_pairs_values))

# print(my_pairs_values)
# for x in my_pairs_values:
#     print(x)

# my_pairs_values_list = list(my_pairs_values)
# print(my_pairs_values_list)

# print(my_pairs_values_list)
# my_pairs_items = my_pairs.items() # returns a list of tuples!
# print(my_pairs_items)  

# [
#   (123, 'number'), 
#   ('name', 'Jones'), 
#   ('address', {'number': 123, 'street': 'Sesame St'})
# ]

# for x,y in my_pairs_items:
#     print(x,y)

# Access nested data
# print(my_pairs)
# street_name = my_pairs["address"]["street"]
# print(street_name)

# You can declare an empty dict
# my_dict = {}

# ========================================

# Tuples (ordered, immutable & allows duplicates)

# my_tup = (1, 2, 3, 3, "hello")
# print(my_tup)

# Immutable means you cannot change the tuple once it's been created: no changing an existing value, no adding new values, no removing values!
# my_tup[0] = "new value"
# print(my_tup[0])
# print(my_tup[-2])

# Loop through the values in the tuple
# for value in my_tup:
#     print(value)

# You CAN reassign a variable to a new tuple, though.
# my_tup = ("WTF", "I'm hungry")
# print(my_tup)

# If you have one value in a tuple, you have to follow it with a comma! Otherwise, Python will think it's a string (because of the double quotes).
# my_little_tup = ("hello",)
# print(isinstance(my_little_tup, tuple))

# print(type(my_little_tup))

# ========================================

# Sets (unordered, unindexed & does NOT allow duplicates)

my_stuff = {"Fred", True, 123, "Jones", "Fred"}
# print(my_stuff) 

# Turn a set into a list, if you want to
# print(list(my_stuff))
# print(my_stuff)

# Turn a list into a set, then back into a list ( a trick for removing duplicate values from your list)
# list_of_names = ["Mary", "Joseph", "Bob", "Joseph"]
# unique_list = list(set(list_of_names))
# print('no dupes!', unique_list)

# Put more stuff into a set
# my_stuff.add("Feed me")
# print(my_stuff)

# You cannot declare an empty set this way. Python will think it's a dictionary.
# my_hmmmm = {}
# so you do this instead
# my_hmmmm = set()
# print("set?", type(my_hmmmm))
# my_hmmmm.add("lonely string")
# my_hmmmm.update(["lonely string", False], {0, 99}, "hi")
# print("set?", my_hmmmm)

# Because sets are unordered and unindexed, you cannot access the individual items in a set. And since you can't access an individual item, that also means you can't change it once it's been added to the set.

# instructors = {"Chase", "Kristen", "Jisie"}
# current_instructor = {"Jisie"}

# Loop over the set
# for person in instructors:
#     print(person)

# Check for item in a collection (applies to lists, dictionaries, tuples and sets)
# if "Jisie" in instructors:
#     print("Yes, Jisie is in this collection")
  
# for person in instructors:
#     if person in current_instructor:
#         print(person)

# ========================================

# For loops

languages = ["HTML", "CSS", "C#", "Javascript", "Python"]
for l in languages:
    if l == "C#":
          # break
        continue
#         # pass (can be used for functions and loops as well)
    # breakpoint()
    print(l)
else:
    print("Graduated from NSS!")
# print("Outside loop")
