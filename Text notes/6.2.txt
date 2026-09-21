"""
(in string, list & tuple as well)
concatenation (in string, list & tuple as well)
    -> + operator
repetition
    -> * operator
membership
    -> in, not in operator
- since we cannot do modification of tuple unlike list (add, remove etc.) but we can do some read operations on tuple, given below (count etc.)
count -> syntax - tuple.count(element)
index -> syntax - tuple.index(element), it's there in string, list also do check
min -> syntax - min(tuple)
max -> syntax - max(tuple)
sum -> syntax - sum(tuple)

student_detail1 = (1001, "John")
student_detail2 = (78.5, 91.0, 83.5, 79.5)
student_details = student_detail1 + student_detail2
print(student_details)

t1 = ("Class 5", 5000)
print(t1 * 3)

print(91.0 in student_detail2)
print(99.0 in student_detail2)
print(91.0 not in student_detail2)
print(99.0 not in student_detail2)
"""
t1 = (10, 4, 1, 9, 0, 3, 1)
print(t1.count(1))

print(t1.index(4))
print(t1[1])
#print(t1.index(40)) error
print(t1.index(1))
# if an item is present multiple times in a string/list/tuple, index functions always give the index of the first occurrence of that element from left side

print(f"Smallest number: {min(t1)}")
print(f"Biggest number: {max(t1)}")
print(f"Total: {sum(t1)}")









