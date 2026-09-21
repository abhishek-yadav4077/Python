"""
doc string
    - used inside function to tell what has done inside the functions
    - first thing to be written in the function, not in middle or last -> error because it's a documentation
"""
# help() -> anything written inside doc string will be visible to user as an output, gives details about any functions
def func():
    """
    This is a doc string
    We can write what the function does here
    :return: None
    """
    return None

print(help(func))


def divide(num1, num2):
    """
    num1: A number to be divided (Numerator)
    num2: A number that divides num1 (Denominator)
    :return: float/ str
    """
    if num2 == 0:
        return "Cannot divide as denominator is 0!"
    else:
        result = num1/num2
        return result

print(help(divide))
print(divide(10, 4))
# help(divide) -> can print without print function

