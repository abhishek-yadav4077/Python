"""
range()
    - built-in function in python which is used to generate sequence of integers in a given interval
    syntax 1:
        range(start, stop(excluded), step)

    syntax in loop:
        for i in range(start, stop, step):
            #statements
    syntax 2:
        range(start, stop) -> step is 1 by default

    syntax 3:
        range(stop) -> both step(1 as default), start(0 as a default)=> 0 to stop-1 with a step of 1
for i in range(1,11,1): #1,2,3,4,5,6,7,8,9,10
    print(i)

#generate odd numbers using range function
for i in range(1,11,2): #1,3,5,7,9
    print(i)

#generate even numbers using range function
for i in range(0,10,2): #0,2,4,6,8
    print(i)

#generate numbers in reverse order
for i in range(20,10,-1): #20,19,18,17,16,15,14,13,12,11
    print(i)

#countdown from 10 to 1(included)
for i in range(10,0,-1):
    print(i)
print("Happy New Year!!!!")

for i in range(1,6): #step is 1 by default
    print(i)

for i in range(5): #start = 0, step = 1
    print(i) #0,1,2,3,4

groceries = ['salt', 'milk', 'sugar']

for index in range(len(groceries)):
    print(index) #fetches index of the list -> 0,1,2
"""
profits = [9, 11, 6, 10]
for index in range(len(profits)):
    quater = index + 1
    # print(index) #generates indexes -> 0,1,2,3
    # print(profits[index]) #generates the value of index -> 9,11,6,10
    print(f"Quarter is: {quater}, Index is: {index}, Profit is: {profits[index]}")
