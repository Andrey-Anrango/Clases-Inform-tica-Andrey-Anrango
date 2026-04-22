"""Parte A. Análisis y comprensión aplicada (30 puntos) 
1. Análisis de datos y código (15 puntos) 
Observa el siguiente código:
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
e) Escribe una instrucción que permita consultar las palabras reservadas de Python. """
# import keyword

"""Parte B. Corrección y construcción de fragmentos (30 puntos) 
3. Corrección de código (15 puntos) 
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


