"""
Simple interest = (P * R * T) / 100
P = Principal amount
R = Rate of interest
T = Time duration
"""
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time duration: "))
si = (principal * rate * time) / 100
print("Simple interest is: ", si)

