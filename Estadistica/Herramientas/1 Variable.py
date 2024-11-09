import numpy as np

X = np.array([22.5, 23.1, 22.5, 24.3, 25.1, 24.8, 23.1, 24.3, 22.9, 24.8, 23.1, 25.1, 23.7, 24.0, 23.4])
media_aritmetica = sum(X) / len(X)
media_geometrica = np.prod(X) ** (1/len(X))
media_armonica = len(X) / sum(1/x for x in X)
cuasivarianza = np.var(X, ddof=1)

X_sort = X.sort()

print (media_aritmetica) #23.78
print (media_geometrica) #23,76
print (media_armonica) #23.74
print (cuasivarianza)
print(X)