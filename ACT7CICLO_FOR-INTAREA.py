#EJERCICIO LISTAS
notas = [8.5, 6.0, 9.0, 7.0, 5.5] 
suma = 0
aprobados = 0
reprobados = 0
for nota in notas:
    suma += nota
    if nota >= 7:
        aprobados += 1
    else:
        reprobados += 1
promedio = suma / len(notas)
print("Suma total de notas:", suma)
print("Promedio del curso:", promedio)
print("Estudiantes aprobados:", aprobados)
print("Estudiantes reprobados:", reprobados)

#EJERCICIOS STRING
contraseña= "Python2026"
letras= 0
num= 0
contador_o= 0
for caracter in contraseña:
    if ('a' <= caracter <= 'z') or ('A' <= caracter <= 'Z'):
        letras += 1
    if '0' <= caracter <= '9':
        num += 1
    if caracter == 'o' or caracter == 'O':
        contador_o += 1
print(f"La cantidad de letras es: {letras}")
print(f"La cantidad de numeros es: {num}")
print(f"La cantidad de letras o es: {contador_o}")

#SET

productos = {"teclado", "mouse", "monitor", "mouse", "impresora"}
contador_productos = 0
mas_de_6letras = 0
for producto in productos:
    contador_productos += 1
    contador_letras = 0
    for letra in producto:
        contador_letras += 1
    if contador_letras > 6:
        mas_de_6letras += 1
print("Cantidad de productos únicos:", contador_productos)
print("Productos con más de 6 letras:", mas_de_6letras)

#Break
correo = input("Ingrese su correo electrónico: ")
usuario = ""
for caracter in correo:
    if caracter == "@":
        break
    usuario += caracter
print("El nombre de usuario es:", usuario)

#CICLO FOR IN RANGE
suma = 0
for i in range(5):
    nota = int(input(f"Ingrese la nota {i+1}: "))
    suma += nota
    promedio = suma / 5
print(f"El promedio de las notas es: {promedio}")
"""-----------------------"""
#rrrr
while True:
    suma = 0
    for i in range(5):
        nota = int(input("Ingrese una nota: "))
        if nota < 2:
            print("No se puede sacar el promedio")
            break
        suma = suma + nota
    else:
        promedio = suma / 5
    print(f"El promedio es: {promedio}")
print("Fin del programa")

num= int(input("Ingrese un número para hallar su tabla de multiplicación: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print("Tabla de multiplicación completa.")
"""---------"""
notas = [5, 8, 9, 7, 10]
cantidad=0
suma=0
for i in range(1, 6):
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