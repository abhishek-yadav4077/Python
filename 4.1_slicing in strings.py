'''
s1 = "Hello World"
print(s1)

length of the string:
print(len(s1))

indexing:
print("First character: ", s1[0])
print("last character: ", s1[-1])

What is slicing ?
- it is a technique where it enables a programmer to access/ fetch a part of a string
- indexing will fetch a single character of a string, but slicing fetch the part word of string
- the output is the substring of a string, the data type itself

Syntax of indexing: string[index]
Syntax of slicing: string[start:end:step]
    - start: starting index at which the slicing operation starts
    - end: ending index at which the slicing stops (excluded)
    - step: integer that specifies the step for the slicing
'''
s1 = "Hello World"
#print(s1[2:7:1])
#print(s1[2:9:2])
s1_slice = s1[1:12:3]
print(s1_slice)
print(type(s1_slice))
