import pandas as pd

# Configura el archivo CSV y el número de fila
input_file = 'C:/Mio/UAX/Estadistica/PISA/Base de datos España.csv'  # Nombre del archivo CSV de entrada
output_file = 'C:/Mio/UAX/Estadistica/PISA/Base de datos España_def.csv'  # Nombre del archivo CSV de salida
fila_referencia = 487779  # Número de fila (base 0) a partir del cual eliminar filas

# Leer el archivo CSV
df = pd.read_csv(input_file)

# Eliminar filas por ENCIMA de la fila de referencia (mantener de la fila 10 hacia abajo)
df_below = df.iloc[fila_referencia:]  # Mantiene las filas desde la número 'fila_referencia' hacia abajo

# Eliminar filas por DEBAJO de la fila de referencia (mantener de la fila 0 a la fila 10)
df_above = df.iloc[:fila_referencia]  # Mantiene las filas desde la primera hasta 'fila_referencia'

# Guardar los resultados en archivos CSV separados
df_below.to_csv('archivo_filtrado_below.csv', index=False)
df_above.to_csv('archivo_filtrado_above.csv', index=False)

print(f"Archivo modificado guardado: archivo_filtrado_below.csv (filas por debajo de la {fila_referencia})")
print(f"Archivo modificado guardado: archivo_filtrado_above.csv (filas por encima de la {fila_referencia})")
