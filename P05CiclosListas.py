#Icker Santiago Alba Ayala
nombres = ["Ana", "Luis", "María", "Carlos", "Sofía"]
print("Lista original:", nombres)
 
# Agregar elemento
nombres.append("Pedro")
print("Después de append:", nombres)
 
# Insertar en posición
nombres.insert(2, "Elena")
print("Después de insert en posición 2:", nombres)
 
# Eliminar elemento
nombres.remove("Luis")
print("Después de remove 'Luis':", nombres)
 
# Acceder por índice
print("Primer elemento:", nombres[0])
print("Último elemento:", nombres[-1])
 
# Longitud
print("Total de elementos:", len(nombres))
 
# Ordenar
nombres.sort()
print("Lista ordenada:", nombres)
 
# Recorrer con índice
print("\nLista numerada:")
for i, nombre in enumerate(nombres, start=1):
    print(f"{i}. {nombre}")
