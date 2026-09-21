"""
- These concepts are for mutable datatypes
"""
import copy #copy mudules used to pass copy function copy()
"""
l1 = [1, 2.5, [10, 20, 30], 'Python']

#shallow copy

l2 = copy.copy(l1)
#both l1 and l2 variables have different memory addresses with same value

l1[0] = 5
l1[2][0] = 50
print(l1, id(l1))
#will l2 change ? #the outer list have the different memory addresses but the inner list have the same memory address, so when there is a change in inner list, the copied list also changed but when there is a change in the outer list, no changes visible in the copied list
print(l2, id(l2))

#deep copy - here the inner list of the copied list also get the different memory locations
l2 = copy.deepcopy(l1)

l1[0] = 5
l1[2][0] = 50
print(l1, id(l1))
#will l2 change ? No
print(l2, id(l2))



shallow copy 
    - creates a new list at a different memory location, the inner elements of the list does not get copied 
    - if any changes made to the nested item/element of the copied list, it does reflected in the original list
deep copy
    - the inner element/ nested list have a different memory location
    - any change in the original list will not get reflected in the copied list
    - can be done to mutable objects as well


d1 = {'id':1111, 'name':'John', 'marks':{'eng':71.5, 'maths':91.5, 'bio':80.0}}
d2 = copy.copy(d1)
d1['name'] = "Dan"
d1['marks']['maths'] = 92.5
print(f"d1 -> {d1}", type(d1))
print(f"d2 -> {d2}", type(d2))


d1 = {'id':1111, 'name':'John', 'marks':{'eng':71.5, 'maths':91.5, 'bio':80.0}}
d2 = copy.deepcopy(d1)
d1['name'] = "Dan"
d1['marks']['maths'] = 92.5
print(f"d1 -> {d1}", type(d1))
print(f"d2 -> {d2}", type(d2))
"""





