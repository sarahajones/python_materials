# -*- coding: utf-8 -*-
"""
Lab 2 and Homework 1 Part 2 Work through
Created on Sun Sep 15 16:03:59 2024

@author: sa4422
"""

import random

# =============================================================================
# Problem 1: Write three short programs that use loops in the following ways:
#
# a) Compute the sum of all numbers between 1 and 100 (inclusive)
# b) Compute the sum of all even numbers between 1 and 100 (inclusive)
# c) The sum of 100 random numbers chosen between 1 and 10 (inclusive)
#
# Problem 2: (a little harder)
# A well-known problem from physics and mathematics is The Drunkard’s walk:
#
# Imagine a city that consists of a grid of streets.
# Now imagine a drunkard that starts at any given intersection of such a grid
# and randomly picks one of four directions to go and then stumbles to the next
# intersection. There they randomly choose one of four directions to go and
# stumble to the next intersection, and so on.  After many such steps, where is
# the drunkard? Intuition may tell us that he shouldn’t be far since the random
# direction choices would ultimately cancel each other out. This is wrong.
#
# We can represent intersections of the grid using Cartesian coordinates (x,y).
# Write a program in Python that begins with the drunkard at the origin (0,0),
# then use a loop to have the drunkard move through 100 intersections.
# Print the ending location and calculate its distance from (0,0).
#
# =============================================================================

# Problem 1
# a) Compute the sum of all numbers between 1 and 100 (inclusive)

x = sum(range(1, 101))


# b) Compute the sum of all even numbers between 1 and 100 (inclusive)
# import numpy as np
# x = np.arange(2, 101, 2)

x = sum(range(2, 101, 2))

# c) The sum of 100 random numbers chosen between 1 and 10 (inclusive)
x = list(range(1, 101))
y = 0

for i in x:
    z = int(random.random()*10)
    y = y + z

# Problem 2: Drunkard's walk

x = 0
y = 0
steps = list(range(1, 101))

for i in steps:
    direction = int(random.random()*2)  # 0 = vertical, 1=horizontal
    magnitude = int(random.random()*2)  # 0=up/right ++, 1 = down/left --

    if direction == 0:
        if magnitude == 0:
            x += 1
        else:
            x -= 1
    else:
        if magnitude == 0:
            y += 1
        else:
            y -= 1
print(x, y)

distance = abs(x)+abs(y)

# =============================================================================
# HW 2: Exercise 1 - palindromes
#
# "I noticed that the last 4 digits were palindromic. DONE
# I drove a mile, and the last 5 were palindromic. DONE
# I drove another mile and the middle 4 were palindromic,
# and the ends were not involved.
# And then one mile later, all 6 digits were palindromic."
#
# The question is, what did the driver see when they first looked?
#
# Use a loop that tries every number between 100000 and 999999 until it finds
# one that meets all of the conditions.
# Specify each condition in the question as a separate boolean expression,
# put them into a bunch of if statements,
# and then put all of that into a while loop.
#
# Your program should do this and then display a message like:
#     "The answer is [the correct answer goes here]!
#
# =============================================================================
starter = list(range(100_000, 999_999))
unsolved = True

x = 0
while unsolved:
    i = str(starter[x])
    if i[-1] == i[-4] and i[-2] == i[-3]:
        # print(f"Start palindrome == {i}")
        j = str(int(i)+1)
        if j[-1] == j[-5] and j[-2] == j[-4]:
            # print(f"Starter == {i}, next step == {j}")
            k = str(int(j)+1)
            if k[-2] == k[-5] and k[-3] == k[-4]:
                # print(f"Starter == {i}, next step == {j}, next step == {k}")
                l = str(int(k)+1)
                if l[-6] == l[-1] and l[-5] == l[-2] and l[-3] == l[-4]:
                    # print(f"Starter == {i}, next == {j}, next == {k}, last == {l}")
                    print(f"The answer is {i}")
                    unsolved = False
    x += 1
# =============================================================================
# HW 2: Exercise 2 - 9 digit looper
# =============================================================================
test1 = 123456789  # solved
test2 = 923456780  # solved
test3 = 987541203  # solved
test4 = 987654321
# THIS SHOULD TAKE A NUMBER AS AN INPUT
# CHECK FOR LEADING ZERO ISSUE

original = test4
unsolved = True
starter = original + 1
while unsolved:
    str_starter = sorted(str(starter))
    for i in range(len(str_starter) - 1):
        duplicates = 0
        if str_starter[i] == str_starter[i + 1]:
            duplicates += 1
    if duplicates == 0:
        str_original = sorted(str(original))
        new_number = 0
        for i in list(range(len(str_original))):
            if str_starter[i] != str_original[i]:
                new_number += 1
        if new_number == 0:
            if len(str_starter) == 9:
                print(f"The solution is number {starter}")
                unsolved = False
            else:
                print("We can't solve this in a 9 digit solution!")
                unsolved = False
        else:
            starter += 1
    else:
        starter += 1
