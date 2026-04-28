a= 3
if a> 0:
    print(f"{a} es positivo")
else:    
    print(f"{a} es negativo")
print("Gracias por usar el programa")
# %%
print("Ingrese tu nota final del curso")
nota= float(input())
if nota >= 90:
    print("A(aprobado)")
else:
    if nota >= 80:
        print("B(aprobado)")
        
    else:    
        if nota >= 70:
            print("C(aprobado)")
        else:
            print("D(reprobado)")
print("Gracias por usar el programa")
# %%
#numero par e impar tambien positivo y negativo.
print("Ingrese un numero para determinar si es par o impar, positivo o negativo")
numero= int(input("Ingrese un numero: "))
if numero==0:
    print("El numero es cero")
else: 
    if numero>0:
        if numero%2==0:
            print("El numero es par y positivo")
        else:
            print("El numero es impar y positivo")
    else:
        if numero%2==0:
            print("El numero es par y negativo")
        else:
            print("El numero es impar y negativo")
print("Fin del programa")

# %%
#Codigo con ELIF
if numero>0 and numero%2==0:
    print("El numero es par y positivo")
elif numero>0 and numero%2==1:
    print("El numero es impar y positivo")
elif numero<0 and numero%2==0:
    print("El numero es par y negativo")
elif numero<0 and numero%2==1:
    print("El numero es impar y negativo")
else:
    print("El numero es cero")
print("Fin del programa")

#Con short hand
print("El número es positivo") if numero>0 else print("El número es negativo") 
print("El número es par") if numero%2==0 else print("El número es impar")
