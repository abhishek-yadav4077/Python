#if-elif-else

marks = float(input("Enter your marks: "))

if marks >= 90:
    print("Grade is O")
    print("Outstanding")
elif 89 >= marks >= 80: #chain expression
    print("Grade is E")
    print("Excellent")
elif 79 >= marks >= 70:
    print("Grade is A")
    print("Very Good")
elif 69 >= marks >= 60:
    print("Grade is B")
    print("Good")
elif 59 >= marks >= 50:
    print("Grade is C")
    print("Good")
elif 49 >= marks >= 40:
    print("Grade is D")
    print("Fair")
else:
    print("Grade is F")
    print("Failed")
print("Thank You")