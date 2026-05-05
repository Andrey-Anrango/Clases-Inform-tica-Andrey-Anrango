clave = ""
while clave != "python123":
    clave = input("Ingrese la clave: ")
print("¡Clave correcta! Bienvenido.")

#------------------------------------------------
# %%
#MENÚ
opción = ""
while opción != "C":
    print("Menú:")
    print("A. Opción A")
    print("B. Opción B")
    print("C. Salir")
    opción = input("Seleccione una opción: ")
    if opción=="A":
        print("Saludos, Bienvenido!")
    elif opción=="B":
        print("Seguimos aprendiendo ciclos while en VSC")
    elif opción=="C":
        print("Saliste del Programa")
    else:
        print("Opción no valida")
print("SE ACABO EL PROGRAMA")

# %%
