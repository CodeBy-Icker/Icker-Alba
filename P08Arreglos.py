#Icker Alba
estudiantes = [
    ["Ana",    [85, 90, 78, 92]],
    ["Luis",   [60, 55, 70, 65]],
    ["María",  [95, 98, 100, 97]],
    ["Carlos", [72, 68, 75, 80]],
]
 
print("=== Reporte de Calificaciones ===\n")
for estudiante in estudiantes:
    nombre = estudiante[0]
    califs = estudiante[1]
    promedio = sum(califs) / len(califs)
    print(f"Estudiante: {nombre}")
    print(f"  Calificaciones: {califs}")
    print(f"  Promedio: {promedio:.2f}")
    if promedio >= 90:
        print("  Estado: ¡Excelente!")
    elif promedio >= 70:
        print("  Estado: Aprobado")
    else:
        print("  Estado: Reprobado")
    print()
 
# Matriz 3x3
print("=== Matriz 3x3 ===")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for fila in matriz:
    print(fila)
print("\nDiagonal principal:", [matriz[i][i] for i in range(3)])
