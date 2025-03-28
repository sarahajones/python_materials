# =============================================================================
# Lab 6  - Monday 10/14/2024 - Text Editing in Python (Lectures 11 and 12)
# Computing in Context 2024: HPM Context - Dr Sarah Ashcroft-Jones

# This script should help bring together the content of Lectures 11&12 and the
# assigned reading of Chapter 11 of "thinkcspy"
# =============================================================================
# 1. 0 Dictionaries - expanded from Lab 5
# maps key to values, a mapping type

# example 1
d = {}  # This makes an empty dictionary
d['apple'] = 'red'
d['banana'] = 'yellow'
d['pears'] = 'green'
d

d.keys()
d.values()

del d['pears']  # to remove a dicitonary entry use "del"
d  # the whole entry for pears is gone
d['apple'] = 'green'  # dictionaries are mutable, can change values for keys
d  # the value for apple has now changed

# example 2
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
inventory['apples']
inventory['pears'] = 0  # mutable
inventory['bananas'] = inventory['bananas'] + 200
inventory['plums'] = inventory['bananas'] * 2

# N.B "in" versus "get"
print('apples' in inventory)
print('cherries' in inventory)

if 'bananas' in inventory:
    print(inventory['bananas'])
else:
    print("We have no bananas")

# looking up a non-existent key can cuase a run_time error
inventory["cherries"]  # this throws an error
print(inventory.get("apples"))
print(inventory.get("cherries"))

print(inventory.get("cherries", 0))    # can set default reurn value

# copying versus alaising
mydict = {"cat": 12, "dog": 6, "elephant": 23, "bear": 20}
yourdict = mydict
yourdict["elephant"] = 999
print(mydict["elephant"])


# =============================================================================
# Reading and writing text files
# NB this code will not run as it does not have the accompanying .txt files
infile = open("filename.txt", "r")
contents = infile.read()  # copy a string out
line = infile.readline()  # alternatively, this just reads a line
infile.close()   # close the stream again, to free up the resource

outfile = open("superfilename.txt", "w")  # new file in write mode
outfile.write("I am adding text now")
outfile.close()  # only actually write to file on close

# to delete or rename files use the os function
import os

# Delete the original coffee.txt file.
os.remove('coffee.txt')

# Rename the temporary file.
os.rename('temp.txt', 'coffee.txt')

# NB:
# A better way to open files is "with open":
# 1. You don't have to worry about closing the files
# 2. "safer" - no resource leak
# 3. more readable

# Using with open we can open a number of files and put the
# processing steps in a block that follows the with statement.
# At the end of the block, the files are closed automatically.

# e.g.
# with open('coffee.txt','r') as coffee_file, open('temp.txt','w') as temp_file:
# have more than one file so separate with comma

# PLEASE NOTE:
# Spend time reading through the lecture 12 notebook output for more info,
# examples, and thoughts on text processing structure and scope.

# =============================================================================
# 3.0 Object reference fun - a thoughtful extra to work through
l1 = [1, 2, 3]
l2 = l1
l2.append(6)  # what happens and why?

# versus
l1 = [1, 2, 3]
l2 = l1[:]  # makes a "shallow dots" copy
l2.append(6)

# but
l1 = [1, [1, 2], 3]
l2 = l1[:]  # shallow dots copy
l2[1].append(100)
# l2 is a shallow copy only

# This is different to reassignment operations e.g. l2[1] = [1,2,100]
# If we mutate we have to think about what the "little dudes" are pointing to
# instead of thinking about it adding a new dude.
# N.B. changing the thing the dudes are pointing to still effects the copy.

# This kind of thinking is also important in functions:


def f(a, x):
    a.append(x)
    x = 0


s = [1, 2, 3]
t = 5

f(s, t)

# s is changed as a side effect based on object reference changes.
# t is unchanged.
# In general, this is bad. Functions shouldn't mutate objects,
# methods can do this but functions should not ... instead:
s = [1, 2, 3]
t = 5


def f(a, x):
    l = a[:]
    l.append(x)
    return l


r = f(s, t)


# =============================================================================