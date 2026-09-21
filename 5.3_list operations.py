'''
extend()
    - very similar to insert() and append()
    - also adds elements at the end of the list
    - append() -> adds only one element at a time
    - extend() -> adds multiple elements at a time, form of square bracket, with comma
    - changes the list itself

fruits = ["Apple", "Mango", "Orange"]
#fruits.append("Banana", "Grapes") error
print(fruits)
print(len(fruits))

fruits.extend(["Banana", "Grapes"])
#fruits.extend("Banana", "Grapes") error
print(fruits)
print(len(fruits))

fruits.append(["Banana", "Grapes"])
print(fruits)
print(len(fruits))
'''
'''
remove()
    - it removes certain elements from the list
    - changes the list itself, not going to create new list unlike string

fruits = ["Apple", "Mango", "Orange"]
print(fruits)
fruits.remove("Mango")
print(fruits)
#fruits.remove("Banana") error

fruits = ["Apple", "Mango", "Orange", "Mango"]
fruits.remove("Mango") #the first occurrence/ value will be deleted
print(fruits)
'''
'''
pop()
    - also used to delete elements from the list
    - takes the index at which the values need to be deleted
'''
fruits = ["Apple", "Mango", "Orange",]
print(fruits)
fruits.pop(2)
print(fruits)
fruits.pop(-1)
print(fruits)

fruits.pop()  #still works, by dafault the last element will be deleted
print(fruits)









