# Lab 4 Solution

# Problem 1: Hamming distance function
# Hamming distance between two equal-length strings of symbols is the number
# of positions at which the corresponding symbols are different.

# For example, the Hamming distance between:
# "karolin" and "kathrin" is 3.
# "karolin" and "kerstin" is 3.
# "kathrin" and "kerstin" is 4.
# 0000 and 1111 is 4.
# 2173896 and 2233796 is 3.

s1 = '1 0 0 1 1'
s2 = '1 0 1 0 0'


def hamming_distance(s1, s2):
    distance = 0
    for index in range(len(s1)):
        if s1[index] != s2[index]:
            distance += 1
    return distance


hamming_distance(s1, s2)


# Problem 2: Palindrome function

test1 = 'madam'
test2 = "adam"
test3 = "kayak"
test4 = "happyhappy"
test5 = "0110"


def is_palindrome(string):
    pattern_length = (len(string)-1)//2
    for index in range(0, pattern_length):
        if string[index] == string[-1-index]:
            palindrome = True
        else:
            palindrome = False
    return palindrome


is_palindrome(test1)
is_palindrome(test2)
is_palindrome(test3)
is_palindrome(test5)
