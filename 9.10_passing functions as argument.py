"""
In python, we can pass values as argument of a function, and we can even pass functions as argument of another functions.
"""
def add_1(number):
    return number + 1

# print(add_1(10))

def square(number):
    return number ** 2

# print(square(4))
num = int(input("Enter a number: "))
result_1 = add_1(num)
result_2 = square(result_1)
print(f"Output is: {result_2}")

#another way -> we are calling a function as an argument inside another function
result = square(add_1(num))
print(f"Output is: {result}")

#we can have multiple functions passed as arguments inside another functions
