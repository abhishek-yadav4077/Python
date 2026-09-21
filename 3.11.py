Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num1 = 100
num1
100

print(num1)
100
print(100)
100
name = "John"
print(name)
John
age = 20
print(age)
20

print(name, age)
John 20
print(name,age)
John 20
print(10,20,30,40,50)
10 20 30 40 50
print(10,20,30,40,50, sep=" ")
10 20 30 40 50
print(10,20,30,40,50, sep="")
1020304050
print(10,20,30,40,50, sep=",")
10,20,30,40,50
print(10,20,30,40,50, sep="#")
10#20#30#40#50
print(10,20,30,40,50, sep="hi")
10hi20hi30hi40hi50

print("Python")
Python
print("Python')
      
SyntaxError: unterminated string literal (detected at line 1)
num1 = 100
      
>>> num2 = 200
...       
>>> result = num1 + num2
...       
>>> print(num1, num2, result)
...       
100 200 300
>>> 
>>> print("Addition of", num1, "and", num2, "is", num3)
...       
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print("Addition of", num1, "and", num2, "is", num3)
NameError: name 'num3' is not defined. Did you mean: 'num1'?
>>> print("Addition of", num1, "and", num2, "is", result)
...       
Addition of 100 and 200 is 300
>>> name
...       
'John'
>>> age
...       
20
>>> print(name, age)
...       
John 20
>>> print("Name:", name, "Age:", age)
...       
Name: John Age: 20
>>> 
>>> day = 10
...       
>>> month=10
...       
>>> year = 2020
...       
>>> print(day, month, year, sep="/")
...       
10/10/2020
