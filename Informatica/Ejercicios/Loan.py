import numpy as np
import matplotlib.pyplot as plt
print ("This program calculates the monthly payement for a loan based on the loan amount, interest rate, and loan term (in months).")
P = (input ("Input the principal loan amount: "))
n = (input ("Input the monthly interest rate: "))
r = (input ("Input the total number of months: "))

#Crear gráfico
fig, ax = plt.subplots(figsize=(10, 6))
M = P(r(r+1)**n) / ((1+r)**n - 1)  #Ecuación de loan
ax.clear()
ax.plot(n, M, label="Monthly payement", color='b')
ax.set_title('Monthly payement for a loan')
ax.set_xlabel('Time (months)')
ax.set_ylabel('Payement ($)')
ax.legend()
ax.grid(True)
plt.show()




