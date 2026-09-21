"""
Modules
    - python files that have some python code written in it
    - we can create our own module by writing some programs, saving them as .py files and using them in another files, that's what is Module
    - we have in-built module in python as well when we install python
    - print(), range(), etc. these are some functions which are pre-imported means we can directly use them without importing explicitly
    - if not pre-imported we have to import it by using import keyword
"""

import random
#random() - it is a function of random module which returns random float between 0.0 and 1.0(excluded)
print(random.random()) #module_name.function_name to call

#randint(a, b) -> returns random integers between a and b (both included)
print(random.randint(10, 15))

nums = [10, 4, 1, 8, 4, 3]
#choice(sequence) -> returns a random item from the sequence
print(random.choice(nums))

fruits = ["Apple", "Orange", "Mango"]
print(random.choice(fruits))

#shuffle(sequence) - returns the elements shuffled in random order
random.shuffle(fruits) #it does print anything(None), it just shuffle things
print(fruits) #shuffled function permanently changes the list

