#Icker Alba
numero_secreto = 7
intentos = 0
adivinado = False
 
print("=== Juego: Adivina el número (entre 1 y 10) ===")
 
while not adivinado:
    intento = int(input("Tu intento: "))
    intentos += 1
 
    if intento < numero_secreto:
        print("Muy bajo, intenta de nuevo.")
    elif intento > numero_secreto:
        print("Muy alto, intenta de nuevo.")
    else:
        adivinado = True
        print(f"¡Correcto! Adivinaste en {intentos} intento(s).")
