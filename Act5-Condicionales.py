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
