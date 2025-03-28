# =============================================================================
# Lab 2  - Monday 09/16/2024 - Advancing in Python (Lectures 3 and 4)
# Computing in Context 2024: HPM Context - Dr Sarah Ashcroft-Jones

# This script should help bring together the content of Lectures 3&4 and the
# assigned reading of Chapters 1,2 & 5 of "thinkcspy"
# =============================================================================
# 1.0 Lists - another data type ###

# Contains multiple values in individual indices (slots)
x = [1, 2, 3, 4, 5]
# Each index can hold a different data type - doesn't all have to be the same
y = [1, "string", True, 7, "word"]


# indexing into lists - indexing starts at 0 to count left to right
x[0]
y[1]
# or can count back from the end (-1 as last item in list)
x[-1]
y[-3]

# =============================================================================
# 2.0 Modules
import math
math.pi  # just contains the value for use
math.sqrt(4)  # also contains some math functions for use

import random
random.random()  # generates number 0-1
int(random.random()*2)  # generates 0 or 1 value
int(random.random()*3)  # generates 0,1, or 2 value

# =============================================================================
# 3.0 if statements - conditionals and logic branching

# if (bool): #(if bool is true)
#  do stuff
# else:# (if bool is false)
#  do this

x = 7
if x == 9:
    print(f"The statement was True: x == {x}")
else:
    print(f"The statement was False: x != {x}")

# can nest if statments inside each other - branching the logic further!
a = 7
if (a < 10):
    if (a > 5):
        print("really really hungry hungry hippos")
    else:
        print("just a little bit hungry hippos")
else:
    print("hippos are quite satisfied")
print("all done")

# =============================================================================
# 4.0 iteration/loops - for and while statements!

# The in keyword
"l" in list  # True
"1" in "123"  # True

# The for statement - building a for loop

# for LOOP_VARIABLE in [SOME KIND OF ITERABLE LIST/RANGE]
#   (indent) do LOOP_BODY

# have all items looped -> no -> take loop var, do loop body, repeat
# if all items have looped -> loop is finished iterating


list = [1, 2, 3, 4]
sum = 0
for i in list:
    # sum += 1
    print(sum)
    print(sum + i)

for i in range(4):
    print(i)

# can combine with an if statement:
for letter in "Gadsby":
    if letter == 'E' or letter == 'e':
        print('This word has an "e"')


# The while statement - building a while loop

# while loop is like a iterative if statement, it loops if statement is True
# Therefore, need to update things in the loop, otherwise get stuck on True
# Must be able to get to place where while statement can be False

a = 10
while (a > 0):
    print(a)
    a = a-1

a = 10
while not (a < 0):  # if don't want zero must update here
    print(a)
    a = a-1
    
    
x = range(1, 101) 
