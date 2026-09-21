"""
What is a dictionary ?
    - it has a key and value pair, comma separated enclosed within curly brackets
    - each key-value pairs are separated by colons
      e.g. {key1:value1, key2:value2, ..........}

Why do we use dictionary ?
    - for our convenience
"""
groceries = {'milk':60, 'biscuits':20, 'rice':90, 'bread':30}
print(groceries, type(groceries))

print(len(groceries))

# print(groceries[0]) error
print(groceries['milk'])

#dictionaries are mutable
groceries['milk'] = 65
print(groceries) #overwrites


groceries['egg'] = 10 #adds new key-value pair to the dictionary groceries
groceries['bread'] = 35 #updates the value of the key in the dictionary groceries
# print(groceries['eggs']) error
print(groceries)
