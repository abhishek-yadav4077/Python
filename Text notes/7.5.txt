num = int(input("Enter a number: "))
"""
if num%2 == 0:
    print("Even")
else:
    print("Odd")
"""
#this same program can be written in 1 line -> ternary operator
#syntax -> true-expression if condition else false-expression
print("Even") if num%2 == 0 else print("Odd")