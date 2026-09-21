Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=1
>>> print(a)
1
>>> a
1
>>> b=2
>>> print(b)
2
>>> c=3
>>> print(c)
3
>>> d=a+b+c
>>> print(d)
6
>>> del d
>>> print(d)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(d)
NameError: name 'd' is not defined. Did you mean: 'id'?
>>> print(a)
1
>>> print(b)
2
>>> print(c)
3
>>> x=5
>>> print(x)
5
>>> x=3
>>> print(x)
3
>>> y=1
>>> z=x*y
>>> print(z)
3
>>> a="python"
>>> print(a)
python
>>> a=1
>>> print(a)
1
>>> _a=1
>>> print(_a)
1
>>> 5=1
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> age=50
>>> print(Age)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(Age)
NameError: name 'Age' is not defined. Did you mean: 'age'?
>>> print(age)
50
>>> a1="hello"
>>> a2=" world"
>>> b=a1+a2
>>> print(b)
hello world
