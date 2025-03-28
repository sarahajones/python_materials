# -----------------------------------------------------------------------------
# Week 3 Lecture notes

# Tuesday Sept 17th
# Thursday Sept 19th

# -----------------------------------------------------------------------------
# Lecture 5
q = [1, 2, 3, 4]
q.append(5)

# vars as reference to some value, so:
r = q
r[0] = 0
q  # changes both

# so if don't want to change it
# we need to make a copy (not a shallow copy) to not overwrite
# slicing a list gives you a copy

2 in q
"ap" in "happy"


def mpg(miles, gallons):
    return miles/gallons

# NB scope of variables and where they exist 

# -----------------------------------------------------------------------------
# Lecture 6
# Functions are where it's at today!

