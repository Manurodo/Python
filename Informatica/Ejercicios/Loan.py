# Input values
P = float(input("Enter the loan amount: "))
r = float(input("Enter the annual interest rate (in %): "))
n = int(input("Enter the loan term (in months): "))
M = (P * r * (1 + r) ** n) / ((1 + r) ** n - 1)

print("The monthly payment is: ", M, "€")




