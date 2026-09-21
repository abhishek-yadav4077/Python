'''
Counting substrings from a string
    - used to count the number of occurences of a substrings/ character inside the string
    - count()
    - syntax - string.count(substring)

s1 = "We are learning Python. Python is fun"
s2 = "Python"
s3 = "e"
print(s1.count(s2))
print(s1.count(s3))
print(f"Occurrences of {s2} is {s1.count(s2)}")
print(f"Occurrences of {s3} is {s1.count(s3)}")

s4 = "learn"
print(s1.count(s4))
'''

'''
Changing case of a string
    - upper(), lower(), title(), capitalize()

s1 = "We are learning Python. Pyhon is FUN!!"
print(s1.upper())
s2 = "Python3.13"
print(s2.upper())

print(s1.lower())
print(s2.lower())

print(s1.title())
print(s2.title())

print(s1.capitalize())
print(s2.capitalize())
'''
#Starting and ending of a string
#startswith() - syntax -> string.startswith(substring)
s1 = "We are learning Python"
print(s1.startswith("W"))
print(s1.startswith("We"))
print(s1.startswith("We are"))

print(s1.startswith("are"))

#endswith() - syntax -> string.endswith(substring)
print(s1.endswith("n"))
print(s1.endswith("Pytho"))



















