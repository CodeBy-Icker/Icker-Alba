#Icker Santiago Alba Ayala
import math
import random
import datetime
 
# --- math ---
print("=== Librería math ===")
print(f"Raíz cuadrada de 144: {math.sqrt(144)}")
print(f"Potencia 2^10: {math.pow(2, 10)}")
print(f"Valor de PI: {math.pi:.5f}")
print(f"Coseno de 0: {math.cos(0)}")
print(f"Factorial de 6: {math.factorial(6)}")
 
# --- random ---
print("\n=== Librería random ===")
print(f"Número aleatorio entero entre 1 y 100: {random.randint(1, 100)}")
print(f"Número aleatorio decimal: {random.random():.4f}")
colores = ["rojo", "azul", "verde", "amarillo", "morado"]
print(f"Color aleatorio de la lista: {random.choice(colores)}")
random.shuffle(colores)
print(f"Lista mezclada: {colores}")
 
# --- datetime ---
print("\n=== Librería datetime ===")
ahora = datetime.datetime.now()
print(f"Fecha y hora actual: {ahora.strftime('%d/%m/%Y %H:%M:%S')}")
print(f"Solo fecha: {ahora.strftime('%d/%m/%Y')}")
print(f"Solo hora: {ahora.strftime('%H:%M:%S')}")
cumple = datetime.date(2000, 6, 15)
hoy = datetime.date.today()
diferencia = hoy - cumple
print(f"Días vividos desde 15/06/2000: {diferencia.days}")
