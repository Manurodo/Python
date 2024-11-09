import matplotlib.pyplot as plt
import numpy as np
X = np.array([1, 2, 3, 4, 5])
Y = [11.5, 34.3, 38.1, 50.2, 55.6]
a, b  = np.polyfit(X, Y, 1)
pearson = np.corrcoef(X, Y)[0, 1]
Y_pred = a*X+b
R2 = pearson ** 2
plt.figure(figsize=(10, 10))
plt.scatter(X,Y)
plt.plot (X,Y_pred, label=f"Recta de regresión: $y = {a:.2f}x$ + ${b:.2f}$ \n Coeficiente de pearson = {pearson:.4f}")
plt.xlabel ("Tiempo de vuelo (s)")
plt.ylabel ("Distancia alcanzada (m)")
plt.legend()
plt.show()

print (f"{pearson}")
print (f"{R2}")

