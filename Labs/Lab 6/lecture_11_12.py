# -----------------------------------------------------------------------------
# Week 6 Lecture notes

# Tuesday Oct 8th
# Thursday Oct 10th

# -----------------------------------------------------------------------------
# Lecture 11

# Object references fun
l1 = [1, 2, 3]
l2 = l1
l2.append(6)

# versus
l1 = [1, 2, 3]
l2 = l1[:]  # makes a copy
l2.append(6)

# but
l1 = [1, [1, 2], 3]
l2 = l1[:]  # shallow dots copy
l2[1].append(100)
# l2 is a shallow copy only

# different to reassignment operations e.g. l2[1] = [1,2,100]
# if mutate what the little dudes are pointing to instead of adding
# a new dude all okay. But changing the thing the dudes are pointing to still
# effects the shallow copy.

# Also important in functions:


def f(a, x):
    a.append(x)
    x = 0


s = [1, 2, 3]
t = 5

f(s, t)

# s is changed as a sideeffect based on opbject reference nonsense
# t is unchanged

# this is bad,functions shouldn't mutate objects,
# methods can do this ... instead:
s = [1, 2, 3]
t = 5


def f(a, x):
    l = a[:]
    l.append(x)
    return l


r = f(s, t)

# reading and writing text files
infile = open("filename.txt", "r")
contents = infile.read() # copy a strong out
infile.close()  # close the stream again, to free up the resource

outfile = open("super.txt", "w") # new file in write mode
outfile.write("I am adding text now")
outfile.close() # only actualyl write to file on close

#text processsing with coffee orders
#param passing and keyword versus positional params, setting initial values

     
