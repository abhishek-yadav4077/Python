"""
filter()
    - it takes a function (lambda is good, another can be use) as a first argument and a sequence as a second argument
    - this offers a very elegant way of filtering out all the elements for particular sequence for which a function returns True
    - it keeps only True part
    syntax:
        filter(function, sequence)

map()
    - it also takes a function (lambda is good, another can be use) as a first argument and a sequence as a second argument
    - it keeps whatever output we get


sequence = [1, 2, 3, 4]
print(sequence)

# odd = lambda x : True if x%2 != 0 else False
# even = lambda x : True if x%2 == 0 else False

#REMEMBER -> we do not call the function odd() rather pass the function as argument odd
filtered_output_odd = filter(lambda x : True if x%2 != 0 else False, sequence)
filtered_output_even = filter(lambda x : True if x%2 == 0 else False, sequence)

print(filtered_output_odd) #output -> <filter object at 0x00000221E35B74C0>
print(f"Odd numbers in the above sequence are: {list(filtered_output_odd)}")

print(filtered_output_even)
print(f"Even numbers in the above sequence are: {list(filtered_output_even)}")
"""



sequence = [1, 2, 3, 4]
print(sequence)

mapped_output= map(lambda x : x**2, sequence)

print(mapped_output)
print(f"Mapped output: {list(mapped_output)}")