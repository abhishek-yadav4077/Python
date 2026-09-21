Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name = "Mark"
name
'Mark'

first_name = input()
John
first_name
'John'
print(first_name)
John

age - input()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    age - input()
NameError: name 'age' is not defined
age = input()
25
print(age)
25
first_name = input("Enter your name")
Enter your nameJill
print(first_name)
Jill

>>> age = input("How old are you? ")
How old are you? 21
>>> print(age)
21
>>> 
>>> num1 = input("Enter a number: ")
Enter a number: 10
>>> num2 = input("Enter another number: ")
Enter another number: 15
>>> print(num1)
10
>>> print(num2)
15
>>> result = num1 + num2
>>> print(result)
1015
>>> type(num1)
<class 'str'>
>>> type(num2)
<class 'str'>
>>> int(num1)
10
>>> int(num2)
15
>>> result = int(num1) + int(num2)
>>> print(result)
25
>>> input = input("What is the current year? ")
What is the current year? 2026
>>> age = input("What is your age? ")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    age = input("What is your age? ")
TypeError: 'str' object is not callable
>>> age2 = input("What is your age? ")
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    age2 = input("What is your age? ")
TypeError: 'str' object is not callable
