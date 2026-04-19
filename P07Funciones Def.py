#Icker Alba
def saludar(nombre):
    """Saluda a una persona por su nombre."""
    print(f"¡Hola, {nombre}! Bienvenido.")
 
def calcular_area_rectangulo(base, altura):
    """Calcula y retorna el área de un rectángulo."""
    return base * altura
 
def es_primo(numero):
    """Determina si un número es primo."""
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True
 
def convertir_temperatura(celsius):
    """Convierte Celsius a Fahrenheit y Kelvin."""
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin
 
# --- Pruebas ---
saludar("María")
 
area = calcular_area_rectangulo(5, 8)
print(f"\nÁrea del rectángulo (5x8): {area}")
 
print("\nNúmeros primos del 1 al 20:")
for n in range(1, 21):
    if es_primo(n):
        print(n, end=" ")
print()
 
f, k = convertir_temperatura(100)
print(f"\n100°C = {f}°F = {k}K")
