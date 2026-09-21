"""
Nested list ?
    - list inside another list

l1 = [5, 1.5, "Python", True, None, [1,2,3], 10]
print(l1)
print(len(l1))
print(l1[-2])

#is it possible to fetch element of internal list of a list ? e.g. 1 from l1
print(l1[-2][0]) #chain indexing
"""
l2 = [[1,2], [3,4], [5,6, [0,1]]]
print(len(l2))
print(len(l2[2]))
print(len(l2[2][2]))

print(l2)
print(l2[2])
print(l2[2][2])
print(l2[2][2][0])


