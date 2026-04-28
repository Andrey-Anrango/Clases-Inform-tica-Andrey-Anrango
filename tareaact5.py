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



