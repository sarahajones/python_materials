# -----------------------------------------------------------------------------
# Week 2 Lecture notes

# Tuesday Sept 10th
# Thursday Sept 12th

# -----------------------------------------------------------------------------
# Lecture 3

x = [3, True, 'happy']

x[0]  # indexing

y = type(x)

len(x)  # but max index 2

x[len(x)-1]  # wrap your brain around that
x[-1]
x[-2]  # backwards steps

y = len(x)  # a value returning function (gives back 3)

# this is unlike print - which does return a value, even if assigned to a var
# print is a display funciton not a value return function

type(type(3))

input("string in string out")

# input is a value returning function - returns a string


fav_float = float(input("Give me the best number ever: "))
print("Best number eva is {:.2f}".format(fav_float))
print(f"Or is it {fav_float:.2f}?")  # nb the f at the start


# program structure
# input from user
# do some computation
# print some output
# demonstrated in the pennies funcitons

# list not properly introduced in the late lectures but assumed


import math  # to import modulus
import random

math.e

random.random()  # calling the funciton random inside module random
# will return a number between 0-1

x = int(2*random.random())  # gives back a 1 or 0

x = int(2*random.random()) + 1  # gives back a 1 or 2

########################################################################
# Lecture 4

# Learning about math module in python.org documentation
# Use instead of chat_gpt or stack_overflow
# algorihtimic flow of operations via condiitional statements - if statements


# if (bool): (if bool is true)
#  do stuff
# else: (if bool is false)
#  do this
# see roshambo file

print(f"text here {var here} more text here")

# constant is just a mneumonic
# identified in capital letters
# reader knows that we will never change the value of these vars they are const

# flow control is NB - which satement is active when and why

# while loops - each time execute check True again each time
# need to update in whle loop otherwise = infinite loop, articulates repitions
# do this until condition becomes true

# for loop -iterating through a list or string

# for x in list:
#  do things

# list = [1,2,3,4,5]
# sum = 0
#    for i in list:
#       print(sum)
#      sum = sum + i

list = [1, 2, 3, 4]
sum = 0
for i in list:
    print(sum)
    print(sum+i)
    # sum.append(sum+i)
# number guessing game

# look at homework 2
# look at lab 2

"l" in list  # True
"1" in "123"  # True

# in only works on ints, gives out True or False

# learn how to spell out Boolean expressions
