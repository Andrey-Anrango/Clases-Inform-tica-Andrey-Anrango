"""NIVEL 1
Solicita datos al usuario usando input("Ingrese su edad: "). 
Si la edad es mayor o igual a 18, muestra: 
→ Tienes la edad suficiente para aprender a conducir. 
Si es menor, indica cuántos años le faltan. """
edad= int(input("Ingrese su edad: "))
if edad>=18:
    print("Tienes la edad suficiente para aprender a conducir.")
else:
    faltan= 18-edad
    print(f"Te faltan {faltan} años para aprender a conducir.")
print("Gracias por usar el programa")

""" Compara las variables my_age y your_age usando if...else. 
Determina quién es mayor. 
Usa input("Ingrese su edad: ") para obtener la edad. """
myage=16
yourage= int(input("Ingrese su edad: "))
if myage>yourage:
    diferencia= myage - yourage
    if diferencia==1:
        print(f"Soy mayor que tú por {diferencia} año.")
    else:
        print(f"Soy mayor que tú por {diferencia} años.")
elif yourage<myage:
    diferencia= yourage - myage
    if diferencia==1:
        print(f"Eres mayor que yo por {diferencia} año.")
    else:
        print(f"Eres mayor que yo por {diferencia} años.")
else:
    print("Tenemos la misma edad. ¡Qué coincidencia!")
print("Gracias por usar el programa")

"""Solicita dos números al usuario. 
Compara:  
o Si a > b → “a es mayor que b”  
o Si a < b → “a es menor que b”  
o Si son iguales → “a es igual a b” """
a= int(input("Ingrese el primer nro: "))
b= int(input("Ingrese el segundo nro: "))
if a>b:
    print(f"{a} es mayor que {b}")
elif a<b:
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es igual a {b}")

"""---NIVEL 2---
Escribe un programa que asigne una calificación según el puntaje:  
90-100 → A 
80-89  → B 
70-79  → C 
60-69  → D 
0-59   → F
"""
print("Ingrese tu nota final del curso")
nota= float(input())
if nota >= 90:
    print("A")
else:
    if nota >= 80:
        print("B")
        
    else:    
        if nota >= 70:
            print("C")
        else:
            if nota >= 60:
                print("D")
            else:
                print("F")
print("Gracias por usar el programa")

"""Solicita el mes al usuario y determina la estación del año:  
o Septiembre, Octubre, Noviembre → Otoño  
o Diciembre, Enero, Febrero → Invierno  
o Marzo, Abril, Mayo → Primavera  
o Junio, Julio, Agosto → Verano """
print("Ingrese el mes para determinar la estación del año")
mes= input("Ingrese el mes: ")
mes= mes.lower()
if mes in ["septiembre", "octubre", "noviembre"]:
    print("Otoño")
elif mes in ["diciembre", "enero", "febrero"]:
    print("Invierno")
elif mes in ["marzo", "abril", "mayo"]:
    print("Primavera")
elif mes in ["junio", "julio", "agosto"]:
    print("Verano")
else:
    print("Mes no válido")
print("Gracias por usar el programa")

"""Dada la lista:  
fruits = ['banana', 'orange', 'mango', 'lemon'] 
Si la fruta ingresada no existe, agrégala a la lista y muéstrala. 
Si ya existe, muestra: 
"Esa fruta ya existe en la lista"""

fruits = ['banana', 'orange', 'mango', 'lemon']
print("Ingrese una fruta para agregar a la lista")
fruta= input("Ingrese una fruta: ")
fruta= fruta.lower()
if fruta in fruits:
    print("Esa fruta ya existe en la lista")
else:
    fruits.append(fruta)
    print(f"Fruta agregada a la lista: {fruits}")   
print("Gracias por usar el programa")

"""Acceso a una plataforma educativa 
Desarrolla un programa en Python que determine el tipo de acceso que tendrá un 
estudiante dentro de una plataforma educativa. 
El programa debe solicitar al usuario tres datos: la edad del estudiante, su 
promedio académico y si cuenta o no con permiso de sus padres. 
Luego, debe aplicar las siguientes reglas: 
• Si el estudiante tiene menos de 12 años, solo podrá ingresar si tiene 
permiso de sus padres.  
o Si tiene permiso, se debe mostrar el mensaje: “Puede ingresar con 
supervisión”.  
o Si no tiene permiso, se debe mostrar el mensaje: “No puede 
ingresar a la plataforma”.  
• Si el estudiante tiene entre 12 y 17 años, el tipo de acceso dependerá de su 
promedio académico:  
o Si el promedio es mayor o igual a 8.5, se debe mostrar: “Acceso 
completo a cursos avanzados”.  
o Si el promedio es mayor o igual a 7 y menor que 8.5, se debe 
mostrar: “Acceso a cursos intermedios”.  
o Si el promedio es menor que 7, se debe mostrar: “Acceso solo a 
cursos básicos”.  
• Si el estudiante tiene 18 años o más, se debe mostrar el mensaje: “Acceso 
libre a la plataforma”.  
El programa debe usar obligatoriamente estructuras if, elif, else y al menos una 
condición anidada."""
print("Ingrese su edad para determinar el tipo de acceso a la plataforma educativa")
edad= int(input("Ingrese su edad: "))
if edad<12:
    permiso= input("¿Cuenta con permiso de sus padres? (sí/no): ")
    permiso= permiso.lower()
    if permiso=="sí":
        print("Puede ingresar con supervisión")
    else:
        print("No puede ingresar a la plataforma")
elif 12 <= edad <= 17:
    promedio= float(input("Ingrese su promedio académico: "))
    if promedio >= 8.5:
        print("Acceso completo a cursos avanzados")
    elif 7 <= promedio < 8.5:
        print("Acceso a cursos intermedios")
    else:
        print("Acceso solo a cursos básicos")
else:
    print("Acceso libre a la plataforma")
print("Gracias por usar el programa")
