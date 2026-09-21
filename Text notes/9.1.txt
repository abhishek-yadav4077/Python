"""
Functions
    - take some arguments and do something for us
built-in functions
    - functions which we get when we install python
    - The python interpreter has a number of functions and types built into it that are always available.
    - print(), len() etc.
some module functions
    - random(), randint(), shuffle() etc.
user defined functions
    - functions which are created or defined by the users
    - a functions is any line of statements which performs a certain task
    - functions are nothing but blocks
Need ?
    - code reusability
"""
#print(argument)
print("Hello World")

var = 1000
print(var)

print(10, 20, 30)

import random
print(random.randint(10,20))

#len()
s1 = "Hello World"
print(len(s1)) #function call

s2 = s1 + " " + "Bye"

l1 = [1, 0, 4, 3]
print(len(l1)) #function call


#is it possible to create a function of its own ? -> Yes
num = 100
if num % 2 == 0:
    print("It is even")
else:
    print("It is odd")

num = 99
if num % 2 == 0:
    print("It is even")
else:
    print("It is odd")
"""
we need to write code again and again
so we need a user-defined function to perform this task for n number of times

how to create user-defined functions ?
syntax:
    def function_name(arg1, arg2, ... argn):
        statement 1
        statement 2
        ...
        statement n
"""

