"""
while True:
    print("Hello World") #infinite loop -> condition is always True

- infinite loop is useful when we want to print something for a large number of times to get the desired result


correct_password = "Python"
while True:
    user_password = input("Enter your password: ")
    if user_password == correct_password:
        print("Password is correct! Congrats.")
        break #break statement is important, if not then the loop will continue forever even the password is correct
    else:
        print("Wrong password, try again")
print("Logged in!")
"""

num = 10 #start
while num<=20: #condition
    print(num)
    num = num + 2 #step

#in while loop, we don't need a range()