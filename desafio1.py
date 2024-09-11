import random

estudiantes = [
    "Estudiante1", "Estudiante2", "Estudiante3"
    ]
materias = [
    "Materia1", "Materia2", "Materia3"
    ]

e = len(estudiantes)
m = len(materias)
matriz = []

for i in range(e):
    fila = [0] * m
    for j in range(m):
        fila[j] = random.randint(1, 10)
    matriz += [fila]

def mostrar_matriz(matriz, estudiantes, materias):
    for i in range(m):
        print(materias[i])
    for i in range(e):
        print(estudiantes[i])
        for j in range(m):
            print(matriz[i][j])
        print()

def calc_prom(matriz):
    for i in range(e):
        suma = 0
        for j in range(m):
            suma += matriz[i][j]
        promedio = suma / m
        print(estudiantes[i])
        print("Promedio:")
        print(promedio)

mostrar_matriz(matriz, estudiantes, materias)
calc_prom(matriz)
