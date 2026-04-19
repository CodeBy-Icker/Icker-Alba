#Icker Alba
def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
        return None
 
print("=== División segura ===")
print(dividir(10, 2))
print(dividir(10, 0))
 
# --- Conversión segura ---
def convertir_entero(valor):
    try:
        return int(valor)
    except ValueError:
        print(f"Error: '{valor}' no es un número entero válido.")
        return None
 
print("\n=== Conversión segura ===")
print(convertir_entero("42"))
print(convertir_entero("abc"))
 
# --- Lectura de archivo segura ---
def leer_archivo(nombre):
    try:
        with open(nombre, "r") as f:
            contenido = f.read()
            print(f"Contenido:\n{contenido}")
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre}' no existe.")
    except PermissionError:
        print(f"Error: No tienes permisos para leer '{nombre}'.")
    finally:
        print("Intento de lectura finalizado.\n")
 
print("\n=== Lectura de archivo segura ===")
leer_archivo("datos.txt")        # no existe → FileNotFoundError
leer_archivo("08c_try_except.py") # este sí existe
 
# --- Múltiples excepciones ---
print("=== Múltiples excepciones ===")
datos = [10, 0, "hola", 5]
for item in datos:
    try:
        resultado = 100 / int(item)
        print(f"100 / {item} = {resultado:.2f}")
    except ZeroDivisionError:
        print(f"Error con {item}: división entre cero.")
    except (ValueError, TypeError):
        print(f"Error con '{item}': tipo de dato inválido.")
