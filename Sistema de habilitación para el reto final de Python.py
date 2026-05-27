clave_correcta = "Python123"
while True:
    clave = input("Ingrese la clave de acceso: ")
    if clave == clave_correcta:
        print("¡Acceso concedido! Bienvenido al sistema de habilitación para el reto final de Python.")
        break
    else:
        print("Clave incorrecta. Inténtalo de nuevo.")
print("Temas evaluados en la unidad")
print("-variables")
print("-calculos")
print("-input")
print("-print")
print("-f-string")
print("-condicionales")
print("-ciclos")
cant_estudiantes= int(input("Ingrese la cantidad de estudiantes a evaluar: "))
for i in range(cant_estudiantes):
    print(f"Evaluando al estudiante {i+1}")
    nombre = input("Ingrese el nombre del estudiante: ")
    nota_ejercicios = float(input("Ingrese la nota de ejercicios básicos: "))
    nota_condicionales = float(input("Ingrese la nota de condicionales: "))
    nota_ciclos = float(input("Ingrese la nota de ciclos: "))
    prácticas= int(input("Ingrese la cantidad de prácticas realizadas: "))
    prom= (nota_ejercicios + nota_condicionales + nota_ciclos) / 3
    if prom >=9:
        if prácticas >= 5:
            estado=("Habilitado con nivel alto")
        else:
            estado=("Pendiente por prácticas")
    elif prom >= 7:
        if prácticas >= 4:
            estado=("Habilitado")
        else:
            estado=("Pendiente por prácticas")
    else:
        estado=("Requiere refuerzo")
    print("---Reporte final del estudiante---")
    print(f"Nombre: {nombre}")
    print(f"Promedio: {prom}")
    print(f"Prácticas realizadas: {prácticas}")
    print(f"Estado académico: {estado}")
print("----FIN DEL PROGRAMA----")

