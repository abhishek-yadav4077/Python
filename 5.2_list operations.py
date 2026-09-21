'''
Slicing of list:
    - very similar to slicing of strings

li = [3, 8, 1, 0, 4, 9, 7, 3, 6]
print(len(li))
print(li[1:6:1])
print(li[2:7:2])


Concatenation of list:
    - very similar to concatenation of strings

l1 = [1, 7, 2]
l2 = [0, 5]
print(l1 + l2)
print(l2 + l1)


#Repetition of lists
print(l2 * 3)


#append()
    - adds an item to the end of the list
    - syntax -> list.append(item)
    - always adds an element at the end of the list

fruits = ["Mango", "Apple", "Orange"]
print(fruits)
print(fruits.append("Banana")) #we got None as an output
print(fruits)

#string
s1 = "Python is fun"
print(s1.replace("Python", "Java"))
print(s1)

    - In strings, we cannot change the existing strings, we always get the new string as a output
    - But in lists, with few functions, we do not get anything in return(None) in the output
    - append() function in list updates the existing list, 
    - actually the list got updated, it does not create a new list, but in string, we got a new string
    - This is called Mutability of list


#insert
    - adds an element before the specified index
    - syntax -> list.insert(index, item)
'''
fruits = ["Mango", "Apple", "Orange"]
print(fruits)
fruits.insert(2, "Banana")
print(fruits)












