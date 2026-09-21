"""
Returning a value
    - we can return a value from a function

def even_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

result = even_odd(9) #the value 9 from the outside function scope get inside function scope
print(result) #None - if function does not return anything, python internally returns None
#Are we getting any value from the above function ? - NO, we are just print something

#if we want to return something - we use return keyword
def even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = even_odd(10)
print(result) #I'm not printing odd or even rather I'm printing odd or even


def add(num1, num2):
    total = num1 + num2
    return total
val_1 = int(input("Enter your number: "))
val_2 = int(input("Enter your number: "))
val = add(val_1, val_2)
print(f"Addition of {val_1} and {val_2} is: {val}")
"""

#Is it possible to return multiple value from a function ? -> YES
def arithmetic(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    return add, sub, mul, div

val_1 = int(input("Enter your number: "))
val_2 = int(input("Enter your number: "))
result1, result2, result3, result4 = arithmetic(val_1, val_2)
print(f"Addition of {val_1} and {val_2} is: {result1}")
print(f"Subtraction of {val_1} and {val_2} is: {result2}")
print(f"Multiplication of {val_1} and {val_2} is: {result3}")
print(f"Division of {val_1} and {val_2} is: {result4}")



