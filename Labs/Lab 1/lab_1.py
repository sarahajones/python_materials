#-------------------------------------------------------------------------------
# Lab 1 - Monday 09/16/2024 - Loops and Conditionals in Python (Lectures 2 and 3)
# Computing in Context 2024: HPM Context - Dr Sarah Ashcroft-Jones

# This script should help bring together the content of Lectures 3&4 as well as the
# assigned reading of Chapters 1 & 2 of "How to Think Like a Computer Scientist"
#-------------------------------------------------------------------------------

### 0.0 The Basics
# Commenting your code?
# This is a comment line, we know this because there is a # at the start of it.
# The hashtag makes Python blind to anything that follows such that it does not try to
# interpret or execute that section as code.
# Because Python does not speak English, but has it's own syntax and language it is
# important to separate out your own notes, and the code you write. We use hashtags to do this.

# In this script, comments will be placed after every line of example code to help explain it.
# This is not just a useful tool for learners, but a fundamental part of programming.
# You need to comment your code to help others (and your future self) understand what you did and why.
# Start the habit early and it will help you forever!


# Let's get started
print("Hello") # your first line of code!
# Highlight this line and hit ">>> Run" above, watch how Python inteprets this
# The function print() will "read" what is inside the brackets and print it to the interpreter
# Note what exactly is printed - the value/tokens inside the quotation marks,
# the quotation marks themselves are not printed.
#-------------------------------------------------------------------------------

### 1.0 Python as a calculator (for ints and floats)
# Run each line (using buttonabove) or copy into your console

# Basic computations: addition and subtraction

2+3

4-2

# Division - automatically floating point, use // as integer division (floor division to integer)

10/5

24//5 #spot the difference in output here!


7 % 3 # the modulus operator % tells you the remainder after integer division is complete

# Multiplication - (and raising to powers/exponents)

6*6

2**2 #to square (or raise to the power of whatever you fancy)
#note the the ^ symbol is not used in this way in python,
#it performs a different kind of operation called bitwise operation (ignore this for now!)

# Basic mathematical functions - in-built code chunks, much like Excel functions

round(44.8)

abs(-22)

# Top tip: check on the order of precedence for different operators here:
# https://runestone.academy/ns/books/published/thinkcspy/Appendices/PrecedenceTable.html#operator-summary
#-------------------------------------------------------------------------------

### 2.0 Other types of data

# Character strings - words and letters (non-numerics)
# Copy and paste these into the interpreter and hit enter to see how they show up

"Hi"

'Hi there'

"Hi," + " how are you doing?" # How did this operation work, how did it handle white space?

"Hello " * 3 # What about this operation - can you predict what might happen?

# Check how long a string is using the len() function (stands for "length")

len('Columbia')


# Moving between other data types - integer, floats, and strings

type("Hi")

int(49.1)
float(49)

# Importantly - numerics can be read as strings, but that changes how Python can work with them:

type('12345')

'12345'/10

int('12345')/10 # here python first executed the function int() and then applied the numeric operators

# Large numbers - a side note on commas, underscores, and readability.
# 1,000,000 versus 1_000_000 - run both digit sets in the interpreter - what happens?
# Why would using underscores be valuable in your code when writing large numbers?
#-------------------------------------------------------------------------------

### 3.0 Variables, Booleans, and Logicals
var = 123 # assign the variable "var" with a value of 123
type(var) # check it's type
var*2 # we can now operate on var accordingly

var = 1234 # we can overwrite a variable
double_it = 2

var*double_it # and we can perform operations with multiple variables


# A note on naming variables - camelCase or under_score, just be consistent
# Also names should be meaningful to you - will the variable names make sense when you look at them next week?


### Logicals and Booleans

# We have already met different numerical values (ints and floats) and str (characters, or character strings).
# A different form of data is a "boolean" type, this can be thought of
# as a True/False statements (the capitalisation matters!).
# A boolean is also known as a bool - THEY ARE NOT STRINGS

# We can evaluate booleans using the equality operator == (the double equals)

print(5 == 5)
print(5 == 6)

# These statements can be useful to assess things like data type
print("5" == 5)

# We can also check if something is "not equal" and return a bool
print("5" != 5)

# In total there are six comparison operators that evaluate to a bool
# x == y, x != y, x > y, x < y, x >= y, x <= y
# Remember - x = y is an assignment, x == y is a comparison operator.

# Beyond boolean operations, evaluating to True or False we also have logicals
# logicals are "and" "or" and "not.
# Logicals and booleans go hand in hand, we use logicals to expand our use of the
# comparison operators and evaluate boolean statements - let's have a look

x = 7
print(x > 0 and x < 10)

n = 25
print(n % 2 == 0 or n % 3 == 0) # we can also have more complex statements
n = 21
print(n % 2 == 0 or n % 3 == 0) # one of these is now true - is that helpful?


# Simplifying via de Morgan's Laws
# not (x and y)  ==  (not x) or (not y)
# not (x or y)   ==  (not x) and (not y)


y = not (x > 0 and x < 10) #operate on the boolean itself, not on integer comparison


#-------------------------------------------------------------------------------

### 4.0 Inputs and inbuilt functions

name = input("Please enter your name: ")
# What value will be in name? What type() will it have?
age = input("How old are you? ")
#How can we make "age" a more useful variable now? Can we use it as it is saved by input()?

#Let's try it:
print("Hi, " + name + "! It's good to meet you. You are " + age + "years old.")

#Your Lab 1 exercise and your Homework 1 part 1 will both rely on this, so get comfy with it now.

#-------------------------------------------------------------------------------

# Lab 1 : In-session Practice exercises (solutions below for hints and help!)

# EXERCISE 1 Learning about Python as a language
# 1. What does the function round() do, what about when the decimel is 0.5? Is it always consistent? Test it out.
# Try the difference between rounding 2.5 and 3.5 - can you distinguish a pattern?

# 2. What's the difference between the round() function and the int() function in the way it "simplifies" numbers?

# EXERCISE 2 (From TP Eds3) Python as a Calculator
# Practice writing arithmetic expressions in Python using the following (use vars to help!)
# 1. How many seconds are there in 42 minutes 42 seconds?

# 2. How many miles are there in 10 kilometers? (There are 1.61 kilometers in a mile)

# 3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace in seconds per mile?


# EXERCISE 3 (From TP Eds 2e): Python Playground, let's make errors
# 1. In a print statement, what happens if you leave out one of the parentheses, or both?

# 2. If you are trying to print a string, what happens if you leave out one of the quotation marks, or both?

# 3. You can use a minus sign to make a negative number like -2. What happens if you put a plus sign before a number? What about 2++2?

# 4. In math notation, leading zeros are ok, as in 09. What happens if you try this in Python? What about 011?

# 5. What happens if you have two values with no operator between them?

#-------------------------------------------------------------------------------

# Lab 1: In-session Practice Exercises: SOLUTIONS

# EXERCISE 1 Learning about Python as a language
# 1. What does the function round() do, what about when the decimel is 0.5? Is it always consistent? Test it out.
# Try the difference between rounding 2.5 and 3.5 - can you distinguish a pattern?
# This requires some reading on wiki - but interesting to look into (if you find these things interesting)!

# 2. What's the difference between the round() function and the int() function in the way it "simplifies" numbers?
# Well, round() actually rounds things, int() just cuts off the floating decimels

# EXERCISE 2 (From TP Eds3) Python as a Calculator
# Practice writing arithmetic expressions in Python using the following (use vars to help!)
# 1. How many seconds are there in 42 minutes 42 seconds?
seconds = (42*60)+42
print(seconds)

# 2. How many miles are there in 10 kilometers? (There are 1.61 kilometers in a mile)
miles = 10/1.61
print(miles)
# 3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace in seconds per mile?
pace = seconds/miles
print(pace)

# EXERCISE 3 (From TP Eds 2e): Python Playground, let's make errors
# 1. In a print statement, what happens if you leave out one of the parentheses, or both?
# Errors but "different" errors! 

# 2. If you are trying to print a string, what happens if you leave out one of the quotation marks, or both?
# As above! Unless you are printing the variable which holds a string, in which case don't use quotes!

# 3. You can use a minus sign to make a negative number like -2. What happens if you put a plus sign before a number? What about 2++2?
# Not a lot - it doesn't "read" it

# 4. In math notation, leading zeros are ok, as in 09. What happens if you try this in Python? What about 011?
# Python doesn't like these either (unless you are dealing with Octals but we are not CS students so we won't!)

# 5. What happens if you have two values with no operator between them?
# Chaos! Errors! Don't do it!


#-------------------------------------------------------------------------------