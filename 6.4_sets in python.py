"""
What are sets ?
    - sets are another datatype of collection of items/elements of different datatypes
    - non-sequential collection (no indexing)
    - comma separated elements enclosed with curly bracket {}

Difference between sets and list/tuple
    - in list/tuple we can have DUPLICATE elements
    - but in set, we don't have
Usage of sets
    - anything that should be unique should be stored in sets
    - identification number of individual

set1 = {10, "Python", 2.5}
print(set1)
print(type(set1))

#cannot have indexing in sets - non sequential, no sequence
# print(set1[0]) error

#Length of the set
print(len(set1))

#slicing also not allowed in sets
"""
#sets do not allow duplicate elements
l1 = [10, 2.5, 10, 30, 10]
print(l1, type(l1))
s1 = {10, 2.5, 10, 30, 10} #it works but the duplicated element counted once
print(s1, type(s1))


