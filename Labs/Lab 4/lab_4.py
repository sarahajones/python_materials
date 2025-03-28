# =============================================================================
# Lab 4  - Monday 09/30/2024 - Advancing in Python (Lectures 7 and 8)
# Computing in Context 2024: HPM Context - Dr Sarah Ashcroft-Jones

# This script should help bring together the content of Lectures 7&8 and the
# assigned reading of Chapter 6, 9&10 of "thinkcspy"
# =============================================================================

# 1.0 Strings

# can add strings together in different ways using +
chars = "String time"
addition = "!"

together = chars + addition

# can also repeat things using *
together3 = chars + (addition*3)

# can index in to strings
s = "python rocks"
print(s[2] + s[-5])


# String methods (functions just for strings)
s.upper()
s.capitalize()

print("*" + s.center(25) + "*")

print(s.find("n"))

# Can slice the string as well!
print(s[3:8])

print(s[7:11] * 3)  # and combine with other operation


# String comparisons (for alphabetising/sorting)

"python" == "python"
"python" < "Python"
"python" > "Python"

"python" < "pythoncode"
"pythoncode" < "Python"
"Pythoncode" < "python"

# Strings are immutable

greeting = "Hello, world!"
newGreeting = 'J' + greeting[1:]
print(newGreeting)
print(greeting)

# Playground - what happens here:
s = "ball"
r = ""
for item in s:
    r = item.upper() + r
print(r)


# 2.0 Lists
# sequential collection of data values (can be strings, or ints, or anything!)
# Strings are similr but only of character values (ordered collections)

l = [1, 2, 3]

# can check length just like strings
len(l)

# can index in just like strings
l[0]

# checking membership using in/not in
alist = [3, 67, "cat", [56, 57, "dog"], [ ], 3.14, False]
print(3.14 in alist)
# what about 
print(56 in alist) 

# can concatenate just like strings
newlist = l + alist

# can slice just like strings
print(alist[1:3])
print(alist[:4])
print(alist[3:])
print(alist[:])

# BUT LISTS ARE NOT STRINGS
# not only can they contain more than just characters, they are also MUTABLE
l = [1, 2, 3]
l[2] = 10
l  # mutable, unlike strings, we cna change it

alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = ['x', 'y']
alist[1:3] = []
alist[1:1] = ['b', 'c']

# more simple than slicing we can delete elements
del alist[1:5]

# objects and references
a = "banana"
b = "banana"

print(a is b)
print(a == b)

a = [81, 82, 83]
b = [81, 82, 83]

print(a is b)
print(a == b)


# alaising
l = [1, 2, 3]
other_list = l
print(l is other_list) # now share same value and same location

l[0] = 100
other_list  # note how changes across lists, "pointers" to the same object

# cloning/making copies
l = [3, 1, 6, 2]
l2 = sorted(l)  # this makes a copy - builds a new object
l2

l = [3, 1, 6, 2]
l.sort()  # changes the object itself so...
l

a = [81, 82, 83]
b = a[:]       # make a clone using slice
print(a == b)
print(a is b)
# =============================================================================
