# Problem 1 Part 1:
test1 = "Happy days are here again!"


def unique_letters(s):
    punctuation = [",", ".", "!", ":", "?", ";"]

    for punc in punctuation:
        s = s.replace(punc, "")

    s = "".join(s.split())
    s = list(set(s.lower()))
    return s


unique_letters(test1)

# Problem 1 Part 2:


def unique_letters2(s):
    s = s.lower()
    s = "".join(s.split())
    s = [char for char in s if char in "abcdefghijklmnopqrstuvwsyz"]
    s = list(set(s))
    return s


unique_letters2(test1)


# Problem 2 Part 1:
import os
curr_path = os.chdir(os.path.dirname((os.path.abspath(__file__))))

def convert_list(input_file, output_file):
    
    with open(input_file, 'r') as input_file, open(output_file, 'w') as output_file:

        word = input_file.readline()

        while word:
            word = word.rstrip('\n')
            word = word.lower()
            
            clean_word = [char for char in word if char in "abcdefghijklmnopqrstuvwsyz"]

            if len(clean_word) == len(word):
                output_file.write(word + '\n')

            word = input_file.readline()

convert_list('wordlist.txt', 'new_wordlist.txt')


# Problem 2 Part 2: 
def length_n(file_name,n):
    # your code here
    with open(file_name, 'r') as input_file:

        my_list = []
        word = input_file.readline()

        while word:
            word = word.rstrip('\n')
            if len(word) == n:
                my_list.append(word)
            word = input_file.readline()
    return my_list


length_n('new_wordlist.txt', 7)


def starts_with(file_name, n, first_letter):
    first_letter = first_letter.lower()
    # your code here
    with open(file_name, 'r') as input_file:

        my_list = []
        word = input_file.readline()

        while word:
            word = word.rstrip('\n')
            if len(word) == n:
                if word[0] == first_letter:
                    my_list.append(word)
            word = input_file.readline()
        return my_list
    
starts_with('new_wordlist.txt', 7, "g")


def contains_letter(file_name, n, included):
    included = included.lower()
    
    with open(file_name, 'r') as input_file:

        my_list = []
        word = input_file.readline()

        while word:
            word = word.rstrip('\n')
            if len(word) == n:
                if word[0] != included:
                    if included in word:
                        my_list.append(word)
            word = input_file.readline()
        return my_list

    
contains_letter('new_wordlist.txt', 15, "g")


def vowel_heavy(file_name, n, m):
    
    with open(file_name, 'r') as input_file:
        vowels = "aeiou"
        my_list = []
        word = input_file.readline()

        while word:
            word = word.rstrip('\n')
            if len(word) == n:
                vowel_word = [vowel for vowel in word if vowel in vowels]
                if len(vowel_word) == m:
                    my_list.append(word)
            word = input_file.readline()
        return my_list


vowel_heavy('new_wordlist.txt', 15, 5)
