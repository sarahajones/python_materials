# -----------------------------------------------------------------------------
# Week 4 Lecture notes

# Tuesday Sept 24th
# Thursday Sept 26th

# -----------------------------------------------------------------------------
# Lecture 7

s1 = "columbia"
s2 = "column"

result = True


def checker(s1, s2):
    for char in s1:
        if char not in s2:
            result = False
            return result


checker(s1, s2)

# top down programming in Python - wishful thinking
# programming pig

# start broad, bullet point it and "wish for functions"
# then make your wish come true, start with low hanging fruit

# for big functions - bullet those out in pseudocode
# migrate to phythonic syntaxed language (still plain English)
# then begin to translate

# build out structure and slowly add in func placeholders
# dividing up the task into segments to be coded

s = "happy\nhappy"  # backslash as an escape sequence
# \n as new line
# \t as tab

# can also use triple quotes ''' string ''' to preserve formatting

# can use triple quotes for doc string comments too in functions
# should tell us if and what it returns

# sentinel is a varable that guards a while loop e.g. "solved", "again", etc.

# -----------------------------------------------------------------------------
# Lecture 8

print('first\n\nsecond')

print('first\t\tsecond')

print('''first
and then
second''')

s = 'Columbia University'
s[0:8]
s[0:8:2]
s[7::-1]  # begin at index 7 and work backwards for teh rest of the string

'adam' in 'madam'
'madam' in 'adam'

'adam' < 'cannon'  # True
'adam' < 'Cannon'  # False

# FUnctions versus Methods

s = 'Columbia University'
type(s)  # function

s.upper()  # method

# other methods: isdigit, split, rstrip, lstrip, replace, count

# LISTS

l = [1, 2, 3]
l[2] = 10
l  # mutable, unlike strings

other_list = l
l[0] = 100
other_list  # note how changes across lists, "pointers" to the same object


l = [3, 1, 6, 2]
l2 = sorted(l)  # this makes a copy - builds a new object
l2

l = [3, 1, 6, 2]
l.sort()  # changes the object itself so...
l

# -----------------------------------------------------------------------------
