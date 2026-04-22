# ===== PARTE A ===== 
"""Observa el siguiente código:
nombre = "Lucía" 
edad = 16 
promedio = 9.75 
cursos = ["Python", "HTML", "CSS"] 
print(type(nombre)) 
print(type(edad)) 
print(type(promedio)) 
print(type(cursos)) 
print(len(nombre))"""
#a) Indica el tipo de dato de cada variable. 
"""str, int, float, list"""
#b) Escribe qué mostraría el programa en pantalla.
"""mostraría el tipo de cada variable aademás de la cantidad de caracteres de la variable nombre""" 
#c) Explica qué hace len(nombre).
"""len(nombre) muestra la cantidad de caracteres que tiene la variable nombre, en este caso 5 caracteres"""

"""2. Comprensión conceptual (15 puntos) 
Responde con tus palabras: 
a) ¿Qué diferencia hay entre print() e input()? 
#print() se utiliza para mostrar info. en pantalla, mientras que input() se utiliza para recibir información que coloca el usuario.
b) ¿Por qué un dato ingresado con input() puede dar error si se usa directamente en un cálculo? 
#Porque input() siempre devuelve una cadena de texto, por lo que si se intenta usar en un calculo u operacón matematica saldrá un error de tipo.
c) Explica la diferencia entre /, // y %. 
#"/" Es la división normal que todos conocemos, "//" es la división entera que devuelve solo la parte entera del resultado, y "%" es el operador de módulo que devuelve el resto de la división entre dos números.
d) Escribe una instrucción que permita comprobar la versión de Python que se está usando. 
# import sys
e) Escribe una instrucción que permita consultar las palabras reservadas de Pythom.
mport keyword"""

# ===== PARTE B ===== 
# Código corregido 
"""3.Corrección de código (15 puntos) 
El siguiente programa tiene errores. Reescríbelo de forma correcta para que funcione. """
ancho = float(input("Ingrese el ancho del terreno: ")) 
largo = float(input("Ingrese el largo del terreno: ")) 
precio = float(input("Ingrese el precio por metro cuadrado: ")) 
area = ancho * largo 
costo = area * precio 
print(f"Área total: {area}")
print(f"Costo estimado: {costo} USD") 
"""Luego responde: 
a) ¿Cuáles eran los errores principales? 
#Los errores principales eran que no se estaban convirtiendo las entradas del usuario a tipo float, causando un error de tipo al intentar realizar operaciones matemáticas con ellas, además el mensaje de salida no estaba formateado correctamente.
b) ¿Por qué tu corrección sí permite obtener resultados válidos?
#Porque al convertir las entradas a tipo float, el programa puede realizar las operaciones matemáticas correctamente y el formato de salida ahora es mas claro"""

"""4. Construcción breve (15 puntos) 
Escribe un fragmento de código que haga lo siguiente: 
1. Cree la variable frase con el texto "Tecnología para todos".  
2. Muestre la frase en mayúsculas.  
3. Muestre la cantidad de caracteres de la frase.  
4. Verifique si la palabra "Python" está dentro de la frase.  
5. Reemplace "Tecnología" por "Programación".  
6. Divida la frase en palabras usando split()."""
frase="Tecnología para todos"
print(frase.upper())
print(len(frase))
print("Python" in frase)
frase_con_modificación=frase.replace("Tecnología", "Programación")
print(frase_con_modificación)
división=frase_con_modificación.split()
print(división)

# ===== PARTE C ===== 
# Programa integrador (40 puntos)
"""5.Desarrollo de Programa) 
Una tienda desea generar un resumen de presupuesto para cubrir una pared rectangular con 
papel decorativo. 
Desarrolla un programa que: 
1. Solicite al usuario: Nombre, apellido, país, ancho de la pared, alto de la pared, precio por 
metro cuadrado  
o Calcule: área de la pared, costo total estimado  
2. Cree la variable nombre_completo.  
1. Muestre un reporte final que incluya: 
o nombre completo, país, área calculada, costo total (La impresión del reporte 
f
inal debe realizarse usando f-strings.) 
3. Muestre además:  
o nombre_completo en mayúsculas  
o la longitud de nombre_completo  
o si la letra "a" está presente en nombre_completo  
o si el costo total es mayor que 100 """

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
pais = input("Ingrese su país: ")
ancho = float(input("Ingrese el ancho de la pared en metros: "))
alto = float(input("Ingrese el alto de la pared en metros: "))
precio_m2=float(input("Ingrese el precio por metro cuadrado: "))
area = ancho * alto
costo_total = area * precio_m2
space= " "
nombre_completo = nombre + space + apellido
print(f"Reporte final:\nNombre completo:{nombre_completo}, país: {pais}, área calculada: {area} m², costo total: {costo_total} USD")
print(nombre_completo.upper())
print(len(nombre_completo))
print("a" in nombre_completo)
print(costo_total > 100) 