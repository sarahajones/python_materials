# =============================================================================
# Lab 5  - Monday 10/07/2024 - Advancing in Python (Lectures 9 and 10)
# Computing in Context 2024: HPM Context - Dr Sarah Ashcroft-Jones

# This script should help bring together the content of Lectures 9&10 and the
# assigned reading of Chapter 10&12 of "thinkcspy"
# =============================================================================
# 1.0 List comprehensions

# Start with an empty list
List = []

# Traditional approach of iterating
for character in 'Happy Monday!':
    List.append(character)
print(List)  # Display list

# Using list comprehension to iterate through loop
List = [character for character in 'Happy Monday!']
print(List)  # Displaying list

# Import required module
import time # this will help us time the two approaches

def for_loop(n):  # function to implement the traditional for loop version
    result = []
    for i in range(n):
        result.append(i**2)  # what does this function do?
    return result


def list_comprehension(n):  # function to implement via list comprehension
    return [i**2 for i in range(n)]


# Calculate time taken by for_loop()
begin = time.time()
for_loop(10**6)
end = time.time()
# Display time taken by for_loop()
print('Time taken for_loop:', round(end-begin, 4))

# Calculate time takens by list_comprehension()
begin = time.time()
list_comprehension(10**6)
end = time.time()
# Display time taken by for_loop()
print('Time taken for list_comprehension:', round(end-begin, 4))


# More examples of list comprehensions
numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers]
print(squared)

List = [character for character in [1, 2, 3]]
print(List)

# can combine with a conditional:
# E.g. new_list=[f(item) for item in old_list if (condition on item)]
List = [i for i in range(11) if i % 2 == 0]
print(List)

# =============================================================================
# 2.0 Dictionaries

# example 1
d = {}  # This makes an empty dictionary
d['apple'] = 'red'
d['cherry'] = 'red'
d['banana'] = 'yellow'
d['pears'] = 'green'
d

d.keys()
d.values()

del d['pears']  # to remove a dicitonary entry use "del"
d  # the whole entry for pears is gone
d['apple'] = 'green'  # dictionaries are mutable, can change values for keys
d  # the value for apple has now changed

d.items()  # gives a clearer print out of the pairings

# example 2
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print(list(inventory.values()))
print(list(inventory.items()))

for (k, v) in inventory.items():
    print("Got", k, "that maps to", v)

for k in inventory:
    print("Got", k, "that maps to", inventory[k])


# example 3
contact = {}
contact['name'] = 'Joe Lion'
contact['phone'] = 2125551212
contact['email'] = 'joe.lion@columbia.edu'
# access the value associated with any key in contact using the array notation
contact['phone']


# =============================================================================
