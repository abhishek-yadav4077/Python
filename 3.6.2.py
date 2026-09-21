Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s1 = "Hello"
s1
'Hello'
int(s1)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    int(s1)
ValueError: invalid literal for int() with base 10: 'Hello'
float(s1)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    float(s1)
ValueError: could not convert string to float: 'Hello'
s2 = "12345"
s2
'12345'
type(s2)
<class 'str'>
int(s2)
12345
y = s2
y
'12345'
type(y)
<class 'str'>
int(y)
12345
y
'12345'

s3=55.34
s3
55.34
str(s3)
'55.34'

s4="Python3.13"
s4
'Python3.13'
float(s4)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    float(s4)
ValueError: could not convert string to float: 'Python3.13'

int('python3')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int('python3')
ValueError: invalid literal for int() with base 10: 'python3'
>>> int('1234a')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    int('1234a')
ValueError: invalid literal for int() with base 10: '1234a'
>>> int(123-')
...     
SyntaxError: unterminated string literal (detected at line 1)
>>> int(123-)
...     
SyntaxError: invalid syntax
>>> int('123-')
...     
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    int('123-')
ValueError: invalid literal for int() with base 10: '123-'
>>> 
>>> language = "Python"
...     
>>> version = 3.13
...     
>>> language + version
...     
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    language + version
TypeError: can only concatenate str (not "float") to str
>>> language + str(version)
...     
'Python3.13'
>>> 
>>> '100' + '100'
...     
'100100'
>>> int('100') + int('100')
...     
200
