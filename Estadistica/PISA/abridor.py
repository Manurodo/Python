import pyreadstat

# Ruta al archivo .sav
input_file = "C:\\Mio\\UAX\\Estadistica\\PISA\\CY08MSP_STU_QQQ.SAV"

output_file = "C:\\Mio\\UAX\\Estadistica\\PISA\\salida.csv"

try:
    # Leer el archivo .sav
    df, meta = pyreadstat.read_sav(input_file)
    
    # Guardar el DataFrame en un archivo CSV
    df.to_csv(output_file, index=False)
    
    print(f"Archivo convertido exitosamente y guardado en {output_file}")
    
except FileNotFoundError:
    print(f"Error: El archivo {input_file} no fue encontrado. Verifica la ruta.")
    
except PermissionError:
    print(f"Error: Permiso denegado al intentar escribir el archivo en {output_file}. Verifica los permisos.")

except Exception as e:
    print(f"Error inesperado: {e}")