"""
student1 = {"marks":80.5, "english":76.0, "phy":89.0}
print(student1)

# fetch the marks for "phy"
print(student1["phy"])
# print(student1["chem"]) error

#get() - it does similar task
print(student1.get("phy"))
print(student1.get("chem")) #no error, got output None
print(student1.get("chem", 40)) #not updating the original dictionary but have a hidden/default value of a key
print(student1)


emp1 = {'id':1001, 'name':'John', 'salary':10000}
print(emp1.get('phone'))
print(emp1.get('phone', 9876543210))
print(emp1.get('id', 9876543210)) #the default value will not return, the actual value returns

#if actual value present then it will return, if not then the default value returns

#Membership operator - in, not in
print('id' in emp1) #True
print('groceries' not in emp1)


#update() - updates the key-value pairs of another dictionary inside the existing dictionary
sem1_marks = {'maths':78.5, 'eng':78.0, 'phy':86.5}
sem2_marks = {'chem':81.5, 'bio':90.5}
sem1_marks.update(sem2_marks)
print(sem1_marks)

groceries_1 = {'milk':60, 'rice':100, 'biscuits':20} #existing dictionary
groceries_2 = {'rice':110, 'bread':30}
groceries_1.update(groceries_2)
print(groceries_1)


#pop() - deletes the both key-value pair from the dictionary
groceries_1.pop('milk')
print(groceries_1)
"""

groceries_1 = {'milk':60, 'rice':100, 'biscuits':20, 'milk':65}
print(groceries_1) #output -> 'milk':65
#keys should not be duplicated in the dictionary, there should be unique keys in the dictionary
#value will be most recent value in that case


