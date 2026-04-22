"""Crea una variable texto con el valor: "Programación Para Todos" - Muestra el contenido de la variable en pantalla.  

Muestra la cantidad de caracteres que tiene la cadena."""

texto = "programación Para Todos"

print("Contenido de la variable:", texto)

cantidad_caracteres = len(texto)

print("Cantidad de caracteres:", cantidad_caracteres)

#Convierte la cadena a mayúsculas. Convierte la cadena a minúsculas. Aplica title() y muestra el resultado. Aplica capitalize() y muestra el resultado.

mayusculas = texto.upper()

print("Mayúsculas:", mayusculas)

minusculas = texto.lower()

print("Minúsculas:", minusculas)

titulo = texto.title()
print("Title:", titulo)
capitalizado = texto.capitalize()
print("Capitalize:", capitalizado)
empieza_con = texto.startswith("Programación")
print(f"¿Empieza con 'Programación'?: {empieza_con}")
termina_con = texto.endswith("Todos")
print(f"¿Termina con 'Todos'?: {termina_con}")
posicion_para = texto.find("para")
print(f"Posición de 'para': {posicion_para}")
contiene_python = "Python" in texto
print(f"¿Contiene 'Python'?: {contiene_python}")

#Reemplaza "Programación" por "Python". Divide la cadena en palabras usando split(). Une las palabras usando " - " como separador.

oracion_modificada = texto.replace("Programación", "Python")
print(f"Reemplazada: {oracion_modificada}")
palabras = oracion_modificada.split()
print(f"Lista de palabras: {palabras}")
resultado = " - ".join(palabras)
print(f"Resultado final: {resultado}")

#Muestra el primer carácter de la cadena. Muestra el último carácter de la cadena. Muestra el carácter en la posición 5.  

print("Primer carácter:", texto[0])
print("Último carácter:", texto[-1])
print("Carácter en posición 5:", texto[5])

#Crea una variable con tu nombre completo. Muestra un mensaje usando format() o f-string: "Hola, mi nombre es ___"  Crea un acrónimo con tus iniciales. Ejemplo: "Juan Pérez" → "JP"

nombre_completo="Andrey Anrango"
print(f"Hola, mi nombre es: {nombre_completo}")
acronimo = "".join([word[0].upper() for word in nombre_completo.split()])
print(acronimo)
