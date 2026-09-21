"""
#Membership operators - in, not in
nums = {1, 3, 2, 0, -1}
print(0 in nums)
print(10 not in nums)

#No concatenation
nums_1 = {1, 3, 2, 0, -1}
nums_2 = {3, 5}
print(nums_1 + nums_2) error

#No repeating of sets
print(nums_1 * nums_2) error


weekdays = ("Mon", "Tue", "Wed", "Thur", "Fri")
print(weekdays)
weekdays = set(weekdays) #overwrites
print(weekdays) #un-ordered set, non-sequential, get different order everytime you run
"""
#Sets are mutable
set1 = {2, 0, -1}
print(set1)
# set1[0] = 10 error, no indexing

#add() - add elements to a set
set1.add(5)
print(set1)
set1.add(0) #no difference on adding duplicate elements
print(set1)

#remove() - removes elements from a set, removes element if present and gives error if not present
set1.remove(0)
print(set1)
# set1.remove(10) error

#discard() - deletes elements from a set, deletes element if present and DO NOT give error if not present
set1.discard(5)
print(set1)
set1.discard(10) #no error
print(set1)











