"""
Tuple
    - similar to list, comma separated elements enclosed within square bracket
    - they are also comma separated elements enclosed within round bracket
    - (item1, item2, item3, ....)
    - sequence of items as a collection

Need ?
    - tuple can also store elements of any datatype like list

tuple vs list ?
    - In list, all functions (append(), extend(), remove() etc.) modifies the original list
    - In tuples, we do not have any of the above functions. we cannot modify a tuple
    - when we create tuple, the elements are fixed

where to use tuple and list ?
    - tuple use where we do not need to modify something
    - list use when there is a scope of modification in the list

t1 = ("Python", 10, 1.5, True, None, [1, 2, 3], (10, 20))
print(t1)
print(type(t1))

print(len(t1))

#Accessing items of a tuple - indexing
print(t1[0])
print(t1[-1])

#slicing of tuple - try it on your own

t1 = (10, 20, 30)
print(t1)
print(type(t1))

t2 = 10, 20, 30, 40, 50   # why it is a tuple, not a list, so round brackets are optional in tuple
print(t2)
print(type(t2))


l1 = [1, 2, 3]
print(l1, type(l1))
t1 = tuple(l1)   #type casting
print(t1, type(t1))
print(l1)   # the original data type remains the same as we know in type casting
"""

fruits = ("Mango", "Orange", "Apple")
print(fruits, type(fruits))
fruits = list(fruits)    #re-assignment
print(fruits, type(fruits))

