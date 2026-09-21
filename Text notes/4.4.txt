'''
- shift + f10 will run the program
s1 = "Python is fun"
print(s1[0])
print(s1[-1])
print(len(s1))

language = "Python"
version = "3.13.3"
print(language + version)
#print("Python" - "P") error

s1 = "Python"
print(s1*3) #In string, '*' operator is a repetition operator

#Membership operators in string
#in, case-sensitive
s1 = "Python is fun"
print("Python" in s1)
print("i" in s1)
print("z" in s1)
print("Java" in s1)

#not in -> reverse of in, case-sensitive
print("Python" not in s1)
print("i" not in s1)
print("z" not in s1)
print("Java" not in s1)

#comparion of strings -> it should exactly match
print("Python" == "Python")
print("Python " == "Python")
'''
#strip() - to remove leading and trailing spaces from a string
s1 = "       Python              "
s2 = s1.strip()
print(s2)
print(s1.strip() == "Python")

# replace() - used to replace a part of a string or a character from a string
s1 = "We are learning Python"
print(s1)
print(s1.replace("Python", "Java"))
print(s1.replace("e", "E"))
print(s1) # original string remains unchanged, we get a new string after replacement
# it replaces by default all character/ substring where ever it finds in entire string

#what if we want to replace only certain number of times
print(s1.replace("e", "E", 1))









