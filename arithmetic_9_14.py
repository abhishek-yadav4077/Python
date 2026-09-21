"""
A simple arithmetic module: arithmetic.py
"""
def add(num1, num2):
    return num1 + num2

def square_root(number):
    return number ** 0.5

"""
__name__ variable
    - it allows us not to run our runnable codes this module is imported and 
     only run this code when this module get executed directly
    
a = 10
b = 20
result = add(a, b), square_root(a)
print(result)
#I don't want these below executable code to run in 9.14_user defined modules.py
"""
#What should I do?
if __name__ == "__main__":
    a = 10
    b = 20
    result = add(a, b), square_root(a)
    print(result)
