"""
while loop
    - it executes a block of statements repeatedly until a given condition is True
    - it terminates when the condition becomes False
    - for loop does not depend on conditions, but while loop depends on conditions
    - that's why called a conditional based loop
    syntax:
        while condition:
            statements
    - its syntax is similar to if statement but if statements only runs once if the condition is True but a while loop keep on repeating a block of statements until the condition becomes False

for i in range(1, 5, 1):
    print(i)
"""
num = 1
while num<5:
    print(num)
    num = num + 1 #if don't do it then stuck in infinite loop
    #while loop does not increment automatically like for loop thats why if not done properly, stuck in infinite loop
