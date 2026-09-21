"""
Modules
    - In Python, a module is a file containing Python code (functions, classes, and variables) with a .py extension that serves as a logical blueprint for organizing and
     reusing logic across applications

Need ?
    - The primary need for modules stems from the core engineering goal of breaking large, unmanageable scripts into smaller, independent, and reusable files.
     Without modules, developers would have to write thousands of lines of code in a single file, making debugging and collaboration impossible.

Why We Need Modules in Python
1.Code Reusability:
    - You can write a complex block of code or function once in a module file and import it into multiple projects without duplicating code.
2.Maintainability and Organization:
    - Modules group related code together. For example, putting database management logic into a database.py file makes it easier to find, update, and manage code.
3.Scoping & Namespace Isolation:
    - Each module establishes its own private namespace. This means functions or variables in different modules can share the exact same names without conflicting or
     overwriting each other.
4.Faster Development with Libraries:
    - Modules allow Python to tap into thousands of built-in features (like math or os) and third-party libraries (like pandas or requests), preventing developers from
    having to reinvent basic operations

Types
    1.Built-in modules
        - available when we install python in our system
        - we have several built-in modules which we need to import to use
        - math, random, datetime, keyword etc.
    2.User defined modules

How to import a module?
    syntax for importing entire functions/variables of a module
        import module_name
    syntax for importing only few functions/variables of a module
        from module_name import func_1, func_2, func_3 ...
    syntax to create an alias for the module that is imported
        import module_name as alias_name -> renaming of module for our convenience

How to use function of a module ?
    syntax:
        module_name.func_name(arg1, arg2, arg3, ...)

#Built-in modules

import math

#Calculate square root of a number, math function have function called sqrt()
num = 100
#output = sqrt(num) error
output = math.sqrt(num)
print(f"Square root of {num} is {output}")

#Calculating the area of a circle
#math module also have variable called pi=3.14...
radius = 5
area_of_circle = math.pi * (radius ** 2)
print(f"Area of circle with radius {radius} is: {area_of_circle}")
print(math.pi)


#throw a die

from random import randint

value = randint(1,6)
print(value)
"""


import datetime as dt
t = dt.time(8, 43, 51)
print(t)




