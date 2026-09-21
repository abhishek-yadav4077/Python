"""
Mutability
    - it is the ability of a value/data to be modified/change
    - lists are mutable
    - after the modification is done, the memory address of list(l1) should be done/not changed (means not resigned into some other variable/value)
Immutability
    - reverse of mutability
    - strings, tuple are immutable

s1 = "Python is fun"
print(s1)
s2 = s1.replace("Python", "Java") #replace() does not modifies the existing string, it creates a new string instead which we store in s2, that's why strings are immutable
print(s2)

t1 = ("Mango", "Orange", "Apple")
t1.append("Banana") error #tuple are immutable
print(t1)

l1 = ["Mango", "Orange", "Apple"] #list are mutable
l1.append("Banana")
print(l1)


#id() - to check memory address
l1 = ["Mango", "Orange", "Apple"]
print(id(l1))
l1.append("Banana")
print(l1)
print(id(l1)) #memory addresses are same, so confirmed that lists are immutable, the state is not changed, it is the existing list which is modified


l1 = ["Mango", "Orange", "Apple"] #lists are re-assignable, just like the below example
print(id(l1))
l1[-1] = "Banana"
print(l1)
print(id(l1))
# x = 10 #python are re-assignable, we can reassign a value of a variable, same for list
# x = 11
# print(x)
"""

fruits = ("Mango", "Orange", "Apple") #tuples are immutable
fruits[-1] = "Banana" #error
print(fruits)

s1 = "Python is fun"
print(s1)
s1[0] = 'p' #error    #strings are immutable
print(s1)

