"""Actividad 3"""
# %%
# Declara tu edad como una variable de tipo entero.
edad = type(int(16))  
# %%
#Declara tu estatura como una variable de tipo decimal (float).  
estatura = type(float(1.64))
# %% 
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area = (base * altura) / 2
print("El área del triángulo es:", area)
# %%
#Escribe un programa que solicite al usuario los lados a, b y c de un triángulo y calcule su perímetro 
ladoa = float(input("Ingrese el lado a del triángulo: "))
ladob = float(input("Ingrese el lado b del triángulo: "))
ladoc = float(input("Ingrese el lado c del triángulo: "))
perimetro = ladoa + ladob + ladoc
print("El perímetro del triángulo es:", perimetro)
# %%
#Obtén la longitud y el ancho de un rectángulo usando un prompt. Calcula su área y su perímetro 
longitud = float(input("Ingrese la longitud del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))   
area_rectangulo = longitud * ancho
perimetro_rectangulo = 2 * (longitud + ancho)
print("El área del rectángulo es:", area_rectangulo)
print("El perímetro del rectángulo es:", perimetro_rectangulo)
# %%

radio = float(input("Ingrese el radio del círcuolo: "))
area_circulo = 3.14*radio**2
circunferencia = 2*3.14*radio
print("El área del círculo es:", area_circulo)
print("La circunferencia del círculo es:", circunferencia)


# %%
#Encuentra la pendiente y la distancia euclidiana entre los puntos (2, 2) y (6, 10).
x1, y1 = (2, 6)
x2, y2 = (2, 10)
pendiente = (y2 - y1) / (x2 - x1)
distancia_euclidiana = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("La pendiente entre los puntos es:", pendiente)
print("La distancia euclidiana entre los puntos es:", distancia_euclidiana)
# %%
"""Calcula el valor de y en la función: 
y = x² + 6x + 9 
Prueba con diferentes valores de x y determina para qué valor de x, y es igual a 0."""
x = float(input("Ingrese el valor de x: "))
y = x**2 + 6*x + 9
print("El valor de y es:", y)
# %%
#Encuentra la longitud de las palabras “python” y “dragón” y realiza una comparación booleana (verdadero/falso). 
palabra1 = "python"
palabra2 = "dragón"
longitud_palabra1 = len(palabra1)
longitud_palabra2 = len(palabra2)
comparacion = longitud_palabra1 == longitud_palabra2
print("La longitud de la palabra 'python' es:", longitud_palabra1)
print("La longitud de la palabra 'dragón' es:", longitud_palabra2)
print("¿Las palabras 'python' y 'dragón' tienen la misma longitud?", comparacion) 
#Usa el operador and para verificar si “on” está presente tanto en “python” como en “dragón”.
presencia_on_python = "on" in palabra1
presencia_on_dragon = "on" in palabra2
presencia_on_ambas = presencia_on_python and presencia_on_dragon
print("¿La subcadena 'on' está presente en 'python'?", presencia_on_python)
print("¿La subcadena 'on' está presente en 'dragón'?", presencia_on_dragon)
print("¿La subcadena 'on' está presente en ambas palabras?", presencia_on_ambas)
#


