import random

estudiantes = ["Estudiante1", "Estudiante2", "Estudiante3"]
materias = ["Materia1", "Materia2", "Materia3"]

e = len(estudiantes)
m = len(materias)
matriz = []

for i in range(e):
    fila = [0] * m
    for j in range(m):
        fila[j] = random.randint(1, 10)
    matriz.append(fila)

def mostrar_matriz(matriz, estudiantes, materias):
    print("      ", end="")
    for materia in materias:
        print(f"{materia:>10}", end=" ")
    print()

    for i in range(e):
        print(f"{estudiantes[i]:<10}", end=" ")
        for j in range(m):
            print(f"{matriz[i][j]:>10}", end=" ")
        print()

def calc_prom(matriz):
    for i in range(e):
        suma = 0
        for j in range(m):
            suma += matriz[i][j]
        promedio = suma / m
        print(f"{estudiantes[i]} - Promedio: {promedio:.2f}")

mostrar_matriz(matriz, estudiantes, materias)
calc_prom(matriz)
