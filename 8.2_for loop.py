"""
s1 = "Hello World"
for char in s1:
    print(char)
print("End of the loop")

#worked with string
#already shown how it works with list, it also works the same way with tuple,sets
"""
#how it will worked with dictionaries ?
employee = {'empid':1001, 'name':'John Gray', 'department': 'HR'}

for i in employee:
    #print(i) #it prints only keys
    #print(i, employee[i]) #chaining #it prints both keys and value
    print(employee[i]) #it prints only values

print(employee.items())

for i in employee.items():
    #print(i)
    #print(i[0]) #prints keys
    #print(i[1]) #prints values
    print(i[0], i[1]) #prints both
