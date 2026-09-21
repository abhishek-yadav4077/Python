Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s1 = "Hello World"
s1
'Hello World'
type(s1)
<class 'str'>
s2 = 'We are learning Python'
s2
'We are learning Python'
type(s2)
<class 'str'>
s3 = """Hello everyone.
We are looking at strings.
Bye"""
s3
'Hello everyone.\nWe are looking at strings.\nBye'
type(s3)
<class 'str'>
s4 = "Python"
type(s4)
<class 'str'>

len(s4)
6
len(s1)
11
len(s2)
22
len(s3)
46
>>> 
>>> s4[0]
'P'
>>> s4[5]
'n'
>>> s4[1]
'y'
>>> s4[2]
't'
>>> 
>>> s4[6]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    s4[6]
IndexError: string index out of range
>>> s1
'Hello World'
>>> len9s10
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    len9s10
NameError: name 'len9s10' is not defined
>>> len(s1)
11
>>> s1[10]
'd'
>>> 
>>> s2
'We are learning Python'
>>> s2[-1]
'n'
>>> s2[-2]
'o'
>>> 
>>> s1+s2
'Hello WorldWe are learning Python'
>>> s1 + " " + s2
'Hello World We are learning Python'
