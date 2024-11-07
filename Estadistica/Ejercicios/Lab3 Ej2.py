import matplotlib.pyplot as plt
import numpy as np
X = np.array([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5])
Y = [920, 610, 455, 360, 300, 260, 225, 200, 180, 165, 150, 140]
a, b = np.polyfit(X, Y, 1)
pearson = np.corrcoef(X, Y)[0, 1]
Y_pred = a*X+b
R2 = pearson ** 2
plt.figure(figsize=(10, 10))
plt.scatter(X,Y)
plt.plot (X,Y_pred, label=f"Recta de regresión: Y = {a:.2f}X + {b:.2f}")
plt.xlabel ("Distancia (m)")
plt.ylabel ("Intensidad de Luz (lux)")
plt.legend()
plt.show()

print (f"{pearson}")
print (f"{R2}")

