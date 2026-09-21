"""
Recursion
    - it is a process in which a function calls itself till a certain condition
    is not met
    - a function which calls itself is a recursive function

Factorial of n
    - Mathematical function
    - represented as n * (n-1) * (n-2) * .... * 3 * 2 * 1
    - n!
    4! = 4 * 3 * 2 * 1 = 24

n! = n * (n-1) * (n-2) * .... * 3 * 2 * 1
   = n * (n-1)!
   = n * (n-1) * (n-2)!

#without recursion
def fact(num):
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1

    return factorial

n = 4
print(f"Factorial of {n} is {fact(n)}")
"""

#With recursion
'''
There are 2 parts to any recursive function
1. Base/terminal condition
    - stop calling itself
2. Recursive function
    - when function calls itself, how it calls 
'''
def fact_rec(num):
    if num == 1:
        return 1
    else:
        factorial = num * fact_rec(num - 1)
        return factorial

print(fact_rec(4))






