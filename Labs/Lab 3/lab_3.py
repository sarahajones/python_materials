# =============================================================================
# Lab 3  - Monday 09/23/2024 - Advancing in Python (Lectures 5 and 6)
# Computing in Context 2024: HPM Context - Dr Sarah Ashcroft-Jones

# This script should help bring together the content of Lectures 5&6 and the
# assigned reading of Chapter 6 of "thinkcspy"
# =============================================================================
# 1.0 Functions

# To build a function you need to define it:
# def function_name()

# the brackets will hold any arguments you need,
# but some functions don't take arguments
# e.g.


def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")


# when called you don't need to insert any arguments,
# but you do need to include the brackets.
# e.g.
print_lyrics()


# Other functions require arguments, you define these as "parameters"
# In the function definition
# e.g.


def print_twice(string):
    print(string)
    print(string)


# To call this function you will then need to input the required argument
print_twice("hello ")

# You can also take a variable as an argument
string = "Nice to see you"
print_twice(string)

# =============================================================================
# 2.0 Value Returning Functions
# Now, while these functions have returned something (because we called print)
# they haven't actually returned any values to us in our environment.

# In order to achieve that we would need "Value Returning Functions"
# Quite simple these use a "return" statement at the end to "output" something
# useful that we calculated inside the function itself!

# e.g.


def square(x):
    y = x * x
    return y


toSquare = 10
result = square(toSquare)
print("The result of", toSquare, "squared is", result)

# Any variables created inside a funcitons are LOCAL to that function
# To access them in the GLOBAL environment you must return them.
# Parameters themselves are also local,
# and do not exist outside the function defintion.


# N.B. Your return statement is the last line of your function ALWAYS
# N.B. A print statement is not a return statement - no value is generated


# =============================================================================
# 3.0 Calling functions (nesting)


def repeat(word, n):
    print(word * n)


spam = 'Spam, '


def first_two_lines():
    repeat(spam, 4)
    repeat(spam, 4)
