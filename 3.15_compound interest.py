"""
Amount = P(1 + R/100) ** T
Compound Interest = Amount - P
"""
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time duration: "))
#Amount1 = principal * (1 + rate/100) ** time
Amount2 = principal * pow((1 + rate/100), time)
ci = Amount2 - principal
print("Amount is: ", round(Amount2, 2))
print("Compound interest is: ", round(ci, 2))