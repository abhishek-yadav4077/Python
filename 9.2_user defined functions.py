"""
def greeting_someone(name):
    print(f"Hello {name}, good morning!")
    print("It's a beautiful day")
#if you run now, no output because we haven't called a function

#calling a functions
greeting_someone("Abhishek")
greeting_someone("Sua")
greeting_someone("John")
greeting_someone("Arun")
greeting_someone("Meena")

#argument - something which we pass to a function and that value will go inside the function and we do something with that

#example2
def even_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_odd(int(input("Enter your number: ")))
"""
#example3
def add(num1, num2):
    total = num1 + num2
    print(total)

add(3, 5)