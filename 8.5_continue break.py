"""
continue, break
    - control statements to control our loops
    - keywords
    - only be used inside a loop, cannot be used outside the loop

for num in range(10):
    if num % 3 == 0: #if the number is divisible by 3
        continue #a loop control keyword that skips the remaining code inside the current iteration and instantly jumps to the beginning of the next cycle
    print(num)
"""
for num in range(1, 10):
    if num % 3 == 0: #if the number is divisible by 3
        break #it terminates/exit the loop
    print(num)