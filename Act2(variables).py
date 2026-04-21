# %%

print(len("Andrey Anrango"))
first_name = "Andrey"
print("first_name length: ", len(first_name))
# %%

first_name = "Andrey"
longitud = len(first_name)
print("first_name length: ", len(first_name))
print(type(first_name))
print(type(longitud))

# %%
primer_nombre, apellido, pais, edad, estado_civil = "Andrey", "Anrango", "Ecuador", "16", "soltero"
# %%
print(primer_nombre)
# %%
print(apellido)
# %%
print(pais)
# %%
print(edad)
# %%
print(estado_civil)
# %%
"""Andrey Anrango
Actividad 2: Nivel 1 y 2
Hoy es 15/4/2026"""
# %%
nombre = "Andrey"
# %%
apelido= "Anrango"
# %%
nombreCompleto="Andrey" + " " +"Anrango"
# %%
pais = "Ecuador"
# %%
ciudad = "Quito"
# %%
edad = "16"
# %%
año = "2026"
# %%
estadoCivil = "soltero"
# %%
esVerdadero = "True"
# %%
luzEncendida = "False"
# %%
nombre, apellido, pais, ciudad = "Andrey", "Anrango", "Ecuador", "Quito"
# %%
"""Nivel 2  """
# %%
type(nombre), type(apellido), type(edad), type(esVerdadero), type(luzEncendida), type(nombreCompleto), type(año), type(estadoCivil), type(ciudad), type(pais)
# %%
nombre = "Andrey"
print("longitud del nombre: ", len(nombre))
# %%
nombre = "Andrey"
apellido = "Anrango"
longitudN = len(nombre)
longitudA = len(apellido)
if longitudN > longitudA:
    print("El nombre es más largo que el apellido")
elif longitudN < longitudA:
    print("El apellido es más largo que el nombre")
else:
    print("El nombre y el apellido tienen la misma longitud")
# %%
NUMERO_UNO = 5
NUMERO_DOS = 4
# %%
#Suma numeroUno y numeroDos y asigna el resultado a una variable llamada total.
numeroUno=5
numeroDos=4
total= numeroUno+numeroDos
print("la suma total es de: ", total)  
# %%
#Resta numeroDos de numeroUno y asigna el resultado a una variable llamada diferencia.  }
diferencia=numeroUno-numeroDos
print("La resta total es de: ", diferencia)
# %%
#Multiplica numeroUno por numeroDos y asigna el resultado a una variable llamada producto.
producto=numeroUno*numeroDos
print("El producto total es: ", producto)
# %%
#Divide numeroUno por numeroDos y asigna el resultado a una variable llamada division.
division=numeroUno/numeroDos
print("La division total es: ", division)
# %%
#Usa el operador módulo para encontrar el residuo de dividir numeroDos para numeroUno y asigna el resultado a una variable llamada residuo.
residuo=numeroDos%numeroUno
print("El residuo es: ", residuo)
# %%
#Calcula numeroUno elevado a la potencia de numeroDos y asigna el resultado a una variable llamada potencia.
potencia=numeroUno**numeroDos
print("El resultado es: ", potencia)
# %%
#Encuentra la división entera de numeroUno para numeroDos y asigna el resultado a una variable llamada divisionEntera.
division_entera= numeroUno//numeroDos
print("La division entera es: ", division_entera)
"""El radio de un círculo es de 30 metros.  
Calcula el área de un círculo y asigna el valor a una variable llamada areaCirculo. Y Calcula la circunferencia de un círculo y asigna el valor a una variable llamada circunferenciaCirculo."""
radio=30
areaCirculo=3.14*radio**2
circunferencia=2*3.14*radio
print("El area del circulo es: ", areaCirculo)
print("La circunferencia es: ", circunferencia)
# %%
#toma el valor del radio como entrada del usuario y calcula el área.
radiotexto=input("Ingrese el radio del circulo")
radio=float(radiotexto)
areausuario=3.14*radio**2
print("El area total es: ", areausuario)
# %%
#Utiliza la función input() para obtener el nombre, apellido, pais y edad de un usuario y almacena cada valor en su variable correspondiente
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
pais = input("Ingrese su país de residencia: ")
edad = int(input("Ingrese su edad: "))
print("Los datos recibidos son: ", nombre, apellido, "de", pais, "con edad de", edad)
# %%
#Ejecuta help('keywords') en la consola de Python o en tu archivo para comprobar las palabras reservadas de Python.
help('keywords')
