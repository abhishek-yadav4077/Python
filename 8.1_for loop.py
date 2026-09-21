"""
Loop
    - doing work repeatedly
    - to repeat a block of program any number of times, we will use loop

Types of loop in python
    1. for loop
        - it is an iterator based loop which steps through the items of a collection like (list, tuple, sets, dict, str), and executes a block of code repeatedly for a number of times equal to the items/elements of that collection
        - syntax:
            for variable in sequence:
                statement 1
                statement 2
                ....
                statement n

    2. while loop
"""
percents = [85.5, 81.0, 86.0, 83.5]
print(percents[0])
print(percents[1])
print(percents[2])
print(percents[3])

for p in percents:
    print(p)

#each repetition is called iteration, in the above example, the loop ran 4 times = length of the list
