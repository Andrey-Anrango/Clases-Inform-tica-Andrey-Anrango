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