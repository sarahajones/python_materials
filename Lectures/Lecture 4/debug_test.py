# load in doctest in case we want to check on things more formally
from doctest import run_docstring_examples


# small function to run doc_test on a function object (reuse me!)
def run_doctests(func):
    run_docstring_examples(func, globals(), name=func.__name__)


# Now let's look at the incorrect version!
def uses_any_incorrect(word, letters):
    """Checks if a word uses any of a list of letters.

    >>> uses_any_incorrect('banana', 'aeiou')
    True
    >>> uses_any_incorrect('apple', 'xyz')
    False
    """
    for letter in word.lower():
        if letter in letters.lower():
            return True
        else:
            return False     # INCORRECT!


#y = uses_any_incorrect("apple", "aeiou")
z = uses_any_incorrect("banana", "aeiou")
print(y)

run_doctests(uses_any_incorrect)



# set up our base function
def uses_any(word, letters):
    """Checks if a word uses any of a list of letters.
    """
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False



# test that function
x = uses_any("apple", "aeiou")

print(x)

# test it formally using doctest
run_doctests(uses_any)

