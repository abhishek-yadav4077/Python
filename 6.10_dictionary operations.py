""""
- not allowed keys - list, sets, dictionary -> mutable datatypes
- allowed keys - strings, integers, floats, boolean, tuple -> immutable datatypes
Therefore, keys of a dictionary can only be MUTABLE datatypes

- values can be any datatypes

d1 = {[1,3,5]:9, [1,2,1]:4} error
print(d1)

d2 = {"Nine":9, "Four":4}
print(d2)

d3 = {1:True, 0:False}
print(d3)

d4 = {1.0:True, 0.0:False}
print(d4)

d5 = {True:1, False:0}
print(d5)

d6 = {(1,3,5):9, (1,2,1):4}
print(d6)

d7 = {{1,3,5}:9, {1,2,1}:4} error
print(d7)

d8 = {{'a':1, 'b':2}:6} error
print(d8)


student1 = {'id':1001, 'name':'John', 'marks':[89.5, 71.5, 81.0]}
print(student1)
#fetch the values
print(student1['marks'])
print(student1['marks'][1]) #chaining
"""

student2 = {'id':1001, 'name':'John', 'marks':{'eng':89.5, 'maths':71.5, 'bio':81.0}}
print(student2)
#fetch the values
print(student2['marks'])
print(student2['marks']['eng']) #chaining

#fetch only the keys
#key()
print(student2.keys(), type(student2.keys()))

#fetch only the values
#value()
print(student2.values(), type(student2.values()))

#items() - fetch key-values pair
print(student2.items(), type(student2.items()))



