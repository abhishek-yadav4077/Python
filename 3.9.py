Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num1 = 100
num2 = 90
num3 = 90

num2 == num3
True
num1 == num2
False
'Python' == 'python'
False
'python' == 'python'
True
num1 != num2
True
num2 != num3
False
num1 > num2
True
num3 > num1
False
num1 < num2
False
num3 < num1
True
num1 >= num2
True
num2 >= num3
True
num2 >= num1
False
num2 <= num1
True
num2 <= num3
True
num1 <= num2
False
True and True
True
>>> True and False
False
>>> Fasle and True
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    Fasle and True
NameError: name 'Fasle' is not defined. Did you mean: 'False'?
>>> False and True
False
>>> False and Fasle
False
>>> False and False
False
>>> 
>>> True or True
True
>>> True or False
True
>>> False or False
False
>>> True not
SyntaxError: invalid syntax
>>> not True
False
>>> not False
True
>>> 
>>> name = "Mark"
>>> age = 25
>>> name == "Mark"
True
>>> name == "Mark" and age >= 18
True
>>> name == "Mark" andage == 30
SyntaxError: invalid syntax
>>> name == "Mark" and age == 30
False
>>> name == "Mark" or age == 30
True
