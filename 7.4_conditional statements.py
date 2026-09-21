"""
if marks >=60, student is pass else student is fail
and the student is pass then we print the grade
"""
#nested if-elif-else

marks = float(input("Enter your marks: "))

if marks >= 60:
    print("Congrats, you have passed the exam")
    if marks >= 90:
        print("Grade is A")
    elif 89 >= marks >= 80:
        print("Grade is B")
    elif 79 >= marks >= 70:
        print("Grade is C")
    else:
        print("Grade is D")
else:
    print("You have failed, study hard next time")

