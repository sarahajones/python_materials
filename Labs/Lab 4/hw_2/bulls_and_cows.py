import random
import math


def generate_secret():
    ''' Generates a 4 digit number with no repeat digits''
    It converts the number to a string and returns it'''
    list_secret = []
    for i in range(0, 4):
        if i == 0:
            list_secret.append(random.randint(0, 9))
        else:
            new_secret = random.randint(0, 9)
            while new_secret in list_secret:
                new_secret = random.randint(0, 9)
            list_secret.append(new_secret)

    secret = ''
    for item in list_secret:
        secret += str(item)

    return secret


def how_many_bulls(guess, answer):
    ''' Returns the number of bulls as an int that the guess earns when the
    secret number is answer. answer and guess should be strings'''
    bulls = 0
    for char in range(0, len(answer)):
        if guess[char] == answer[char]:
            bulls += 1
    return bulls


def how_many_cows(guess, answer):
    ''' Returns the number of cows as an int that the guess earns when the
    secret number is answer. answer and guess should be strings'''
    cows = 0
    duplicates = 0
    for char in range(0, len(answer)):
        if guess[char] in answer and guess[char] != answer[char] and guess.count(guess[1]) == 1:
            cows += 1
        elif guess[char] in answer and guess[char] != answer[char] and guess.count(guess[1]) > 1:
            cows += 1
            duplicates += guess.count(guess[1])
    cows = cows - math.sqrt(duplicates)
    return int(cows)
