# This is the basic blueprint for using a generator object to generate every possible password of a given length using a given character set.

import itertools
import string

def passwordGenerate(characterSet, length):                             # this function returns a generator object yielding each possible combination in sequence
    for combination in itertools.product(characterSet, repeat=length):
        yield ''.join(combination)

characterSet = string.ascii_letters + string.digits             # add in punctuation and special characters as needed

passwords = passwordGenerate(characterSet, 10)

for _ in range(100):
    nextPass = next(passwords)
    print(nextPass)