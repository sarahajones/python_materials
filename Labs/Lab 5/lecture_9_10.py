# -----------------------------------------------------------------------------
# Week 5 Lecture notes

# Tuesday Oct 1st
# Thursday Oct 3rd

# -----------------------------------------------------------------------------
# Lecture 9

# Strings
# 1. strings are immutable
# 2. strings are iterable

s1 = "happy"

for stuff in s1:
    print(stuff)

# can slice strings, and pull out substrings
s1[1:4]  # go to one before the 4th index (4-1 long)

s1[:4]
s1[:]
s1[1:]
s1[1:5:2]
s1[::2]

s1[::-1]
s1[:-5:-1]

# string methods, the actions we can do to the datatype/class
s1.upper()
# can't change s1 unless you reassign it / save over s1

# variables which refer to objects are object reference aka all vars in python

'joe'.upper()

s2 = "happy happy fun times"
s2.split()
s2.split("p")

s2.rstrip("s")  # strip off things sitting on the right hand side

s2.replace("p", "m")

# Lists
# another sequenced iterable collection, but differences
# indexing and slicing the same

# but are collections of object references so mutable and references can
# get mixed up

t = [1, 4, 6, 7, 2, 3, 5]
sorted(t)  # this function, and others, do not mutate the object itself

t.sort()  # but the method operates on the object itself, and mutates it.
# (lists are mutable so this is possible)

l2 = [1, 3, 4, 8, 9, 10]
t = [x ** 2 for x in l2 if x % 2 == 0]

s = "I need a sentence to splice based on vowels"
vowels = [v for v in s if v in "aeiouAEIOU"]


# -----------------------------------------------------------------------------
# Lecture 10

# list comprenhensions - they are powerful

s = "Hay man, this is my strong"
# if i want to get the vowels out, I could do a for loop
vowels = []

for char in s:
    if char in "aeiouAEIOU":
        vowels.append(char)

# OR could use list comprehension for this in a more compact wat
# more computationally efficient

v2 = [letter for letter in s if letter in 'aeiouAEIOU']
# they can hold an iterative and a conditional statement, can also do function

l2 = [3, 2, 5, 8, 10, 12, 9]

# if want the squares of the odd numbers

l3 = [number**2 for number in l2 if number % 2 == 0]


# dictionary 
# think of it as pairs of numbers, key plus value pairs

d = {}  # set with pairs of curly braces
# populate
d = {'apple': 'red', 'cherry': 'red', 'banana': 'yellow'}
d['apple']
d['banana']

# to add a key
d['orange'] = 'orange'
d

# rules: keys must be immutable - i.e. strings
# values on the otherhand can be anything
# keys have to be unique, but values do not

d.keys()
d.values()

contact = {}
contact['name'] = "Mickey"
contact['phone'] = "123456789"
contact['email'] = 'mickey@disney.com'

contact2 = {}
contact2['name'] = "Minnie"
contact2['phone'] = "123456788"
contact2['email'] = 'minnie@disney.com'

mycontacts = {}
mycontacts[contact['name']] = contact
mycontacts["Mickey"]
mycontacts["Mickey"]['phone']

mycontacts = {contact['name']: contact, contact2['name']: contact2}
mycontacts

# just like a list of lists
listfun = [1, 2, [1, 2, 3]]
listfun[2][2]

# SETS
# unordered collections of stuff
x = set() # this is how you set an empty set
a = {1, 5, 3} # note can't make empty sets with {} as will read a dict
a #shift automatically to new order
# so can iterate through, but the order may not be what be what we expect. 
#
a = {1 ,3 ,3 , 5, 3, 1}
# all the repeats will disappear
# as it is a collection of unordered stuff (unique)
# can interesect and union etc
s = "happy"

set(vowels)

b = {10, 1, 2, 5, 5, 6, 2, 3, 6}

a & b  # intersection
a.intersection(b)
a | b  # union
a.union(b)

a - b
b - a  # difference
a ^ b  # symmetrical difference
(a | b) - (a & b)  # longhand symmetrical difference

# also super set, strict super set, subset etc... basic set operators.
