num= int(input("Ingrese un número para hallar su tabla de multiplicación: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print("Tabla de multiplicación completa.")
"""---------"""
notas = [5, 8, 9, 7, 10]
cantidad=0
suma=0
for i in range(1, 4):
    suma=suma+notas[i]
    cantidad= cantidad+1
promedio =suma/cantidad
print(f"El promedio de las notas es: {promedio}")
"""---------"""

# %%
# Programa para generar una tabla de multiplicar
# usando solo los factores pares: 2, 4, 6, 8 y 10
numero = int(input("Ingrese un número: "))
for i in range (2, 11, 2):
    resultado= numero*i
    print(f"{numero}x{i} = {resultado}")
# %%
numero = int(input("Ingrese un número: "))
for i in range (9, 0, -2):
    resultado= numero*i
    print(f"{numero}x{i} = {resultado}")
# %%
# Asignar estudiantes a los puestos de un laboratorio
# El laboratorio tiene 3 filas y 4 computadoras por cada fila
# Ciclo externo: recorre las filas del laboratorio
# range(1, 4) genera los valores 1, 2 y 3

nombre = ["Ana", "Luis", "María", "Carlos", "Sofía", "Mateo", "Daniela", "Pedro", "Valeria", "José", "Camila", "Andrés"]
indice = 0  
for fila in range(1, 4):
    # Recorrer computadoras
    for computadora in range(1, 5):
        print(f"{nombre[indice]} asignado a Fila {fila} - Computadora {computadora}")
        indice += 1
    print(f"Fin de la fila: {fila}")
print("Fin del programa")

