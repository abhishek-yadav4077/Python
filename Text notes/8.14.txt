"""
Create a simple number guessing game.
The user gets 10 chances to guess a number.
if the user guesses the number before 10 chances, stop asking the number from the user, say Congrats and end the game
if the user never guesses the number, ask then 10 times and then end the game!!
"""
import random
num = 1

print("Welcome to the number guessing game. We have a number that needs to be guessed. You have 10 attempts.")
print("The secret number is between 1 and 50")

secret_number = random.randint(1,50)

attempts = 10
is_guess_correct = False

while num <= 10:
    print(f"You have {attempts} attempts remaining.")
    user_number = int(input("Enter your guess: "))
    if user_number == secret_number:
        print("Congrats, your guess is correct!")
        is_guess_correct = True
        break
    else:
        if user_number < secret_number:
            higher_or_lower = "higher"
        else:
            higher_or_lower = "lower"
        print(f"Your guess is wrong! Try {higher_or_lower} number.")
        print("Your guess is wrong!")

    num += 1
    attempts -= 1

if not is_guess_correct:
    print("Bad luck!! You exhausted all your attempts and couldn't guess the number")
print(f"The secret number was {secret_number}. GAME OVER!!")