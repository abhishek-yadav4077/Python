"""
raise
    - to raise an exception followed by the name of the exception

salary = float(input("Enter your salary: "))

if salary < 0:
    raise ValueError("Salary cannot be negative!")
else:
    print(f"Your salary is: {salary}")
"""

age = float(input("Enter your age: "))

if age < 0:
    raise Exception("Age cannot be negative!") #all handling/ runtime errors come under this
else:
    if age >= 18:
        print("You can vote")
    else:
        print("You cannot vote")

