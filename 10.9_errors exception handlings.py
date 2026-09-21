"""
In python, we have two classifications of errors
    1.Compile time error
        (i)Syntax error
            - issue with the syntax
        (ii)Indentation error
            - issue with the indentation

    2.Runtime error/ Exceptions
        - if the code is syntactically correct but still issue
        - while running a program, errors can be detected -> exceptions (errors during execution)
        e.g. zero division error, file exist error etc.

        (i)Built-in exceptions
            - errors that we get when there is an issue with the program and python identifies that issue
            and gives to us
            e.g. name error, value error, index error, key error etc.

age = 24
print(age  #syntax error

age = 24
if age >= 18:
print("You are an adult!")  #indentation error


print(10/0) #ZeroDivisionError, runtime error

x = 100
result = x + y #NameError, runtime error
print(result)


#How to handle these exceptions ?
- try-except block

try -> it is a block under which we write the program that needs to be executed,
       and we can aspect an error over there
except -> it is a block wherein we are inspecting that there could be an error
        if there is an error in try block, the program flow should to the except block
"""

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1/num2
    print(result)
except ZeroDivisionError:
    print("The denominator cannot be 0")
except ValueError:
    print("Input should only be digits")



