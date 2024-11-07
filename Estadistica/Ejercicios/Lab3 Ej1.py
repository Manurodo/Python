import numpy as np
import matplotlib.pyplot as plt
X = np.array([1.2, 2.3, 3.1, 1.5, 2.6, 3.3, 1.8, 2.9, 3.6, 1.0, 2.1, 3.2, 1.6, 2.4, 3.4, 1.9, 2.5, 3.0, 1.4, 2.7, 3.5, 1.1, 2.2, 3.7, 1.7, 2.8, 3.8, 1.3, 2.0, 3.9])
Y = [1.3, 5.4, 9.1, 2.2, 6.8, 9.7, 3.1, 8.4, 11.0, 0.9, 4.5, 9.5, 2.8, 6.3, 10.3, 3.7, 6.9, 8.9, 2.1, 7.6, 10.8, 1.1, 5.0, 11.5, 3.0, 8.0, 12.0, 1.8, 4.0, 12.3]
correlacion = np.corrcoef(X, Y)[0, 1]
a, b = np.polyfit(X, Y, 1)
Y_pred = a * X + b
Y_mean = np.mean(Y)
SCE = np.sum((Y_pred - Y_mean) ** 2)
SCT = np.sum((Y - Y_mean) ** 2)
R2 = SCE / SCT

plt.figure(figsize=(10, 10))
plt.scatter(X, Y, s=50)
plt.plot (X,Y_pred, label=f"Recta de regresión: Y = {a:.2f}X + {b:.2f}")
plt.xlabel ("Velocidad (m/s)")
plt.ylabel ("Energía Cinética (J)")
plt.title ("Representacion grafica Velocidad, Energía Cinetica")
plt.legend ()
plt.show()

print(f"Pendiente (m): {b:.2f}")
print(f"Intersección (b): {a:.2f}")