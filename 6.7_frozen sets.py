s1 = {1, 2, 4, 0}
s1.add(-1) #shows sets are mutable
print(s1, type(s1))

#frozen sets are immutable sets
fs1 = frozenset({10, 20, 30})
print(fs1, type(fs1)) # output - frozenset({10, 20, 30}) <class 'frozenset'>

# fs1.add(40) error
# print(fs1)

#we cannot have add, remove, append etc. but we can have union, intersection, difference
fs2 = frozenset({10, 50, 100, 200})
print(fs2, type(fs2))

print(fs1 & fs2)
print(fs1 | fs2)
print(fs1 - fs2)
