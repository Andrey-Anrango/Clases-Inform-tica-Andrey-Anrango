def generate_full_name():
    first_name="Andrey "
    last_name="Anrango"
    full_name=first_name + last_name
    print(full_name)
generate_full_name()
print("----")
generate_full_name()


# EJEMPLO 1: Registro
def mostrar_instrucciones():
    print("=== INSTRUCCIONES DEL PROGRAMA ===")
    print("1. Ingresa tu nombre.")
    print("2. Ingresa tu edad.")
    print("3. El programa mostrará un mensaje personalizado.")
def mostrar_despedida():
    print("Gracias por usar el programa.")

print("=== SISTEMA DE REGISTRO ===")
opcion = input('¿Deseas ver las instrucciones? si/no: ')
if opcion == 'si':
    mostrar_instrucciones()
nombre = input('Ingrese su nombre: ')
edad = input('Ingrese su edad: ')
print(f'Hola {nombre} tienes {edad} años.')
mostrar_despedida()


# EJEMPLO 2: Suma
def mostrar_instrucciones():
    print("=== INSTRUCCIONES ===")
    print("Debe ingresar dos números.")
    print("El programa sumará esos números.")
    print("Puede escribir ayuda si no entiende qué hacer.")

print("=== SUMA DE DOS NÚMEROS ===")
mostrar_instrucciones()
dato = input('Ingrese el primer número o escriba ayuda: ')
if dato == 'ayuda':
    mostrar_instrucciones()
    dato = input('Ingrese el primer número: ')
numero1 = int(dato)
numero2 = int(input('Ingrese el segundo número: '))
suma = numero1 + numero2
print(f'La suma es: {suma}')

def saludar(nombre):
    print(f"Hola {nombre}, bienvenido al curso de Python.")
saludar("Andrey")

# %%
def mostrar_estudiante(nombre, curso):
    print("Estudiante registrado:")
    print("Nombre:", nombre)
    print("Curso:", curso)
    print("---------------------")
def mensaje_final():
    print("Fin del programa")
cantidad = int(input("¿Cuántos estudiantes desea ingresar? "))
contador = 0
while contador < cantidad:
    print("\nRegistro del estudiante", contador + 1)
    nombre = input("Ingrese el nombre del estudiante: ")
    curso = input("Ingrese el curso del estudiante: ")
    mostrar_estudiante(nombre, curso)
    contador += 1
mensaje_final()
# %%
# EJEMPLO 3:
def calcular_promedio(nota1, nota2, nota3, name, apellido):
    promedio = (nota1 + nota2 + nota3) / 3
    print(f"El promedio de las notas es de: {name} {apellido}. es {promedio}")
nombre= input("Ingrese el nombre del estudiante: ")
apellido1= input("Ingrese el apellido del estudiante: ")
notas1 = float(input("Ingrese la primera nota: "))
notas2 = float(input("Ingrese la segunda nota: "))
notas3 = float(input("Ingrese la tercera nota: "))
print("---Resultado---")
calcular_promedio(notas1, notas2, notas3, nombre, apellido1)
# %%
#CON RETTORNO SIN PARAMETROS
def obtener_mensaje():
    mensaje = "¡Hola! Bienvenido al sistema."
    return mensaje  
def generar_nombre_completo(nombre, apellido):
    nombre_completo = f"{nombre} {apellido}"
    return nombre_completo
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
print(obtener_mensaje())
print(generar_nombre_completo(nombre, apellido))
# %%
#TAREA:
def calcular_total_producto(precio, cantidad):
    return precio * cantidad
print("=== SISTEMA DE COMPRA ===")
subtotal = 0 
for i in range(1, 4):
    print(f"\nProducto {i}")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    while precio <= 0:
        print("Precio no válido. Debe ser mayor que 0.")
        precio = float(input("Ingrese nuevamente el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad comprada: "))
    while cantidad <= 0:
        print("Cantidad no válida. Debe ser mayor que 0.")
        cantidad = int(input("Ingrese nuevamente la cantidad comprada: "))
    total_producto = calcular_total_producto(precio, cantidad)
    subtotal += total_producto
    print(f"Producto registrado: {nombre}")
    print(f"Total del producto: ${total_producto:.2f}")
iva = subtotal * 0.15
total_pagar = subtotal + iva
print("\n=== RESUMEN DE COMPRA ===")
print(f"Subtotal: ${subtotal:.2f}")
print(f"IVA (15%): ${iva:.2f}")
print(f"Total a pagar: ${total_pagar:.2f}")


# %%
#EJERCICIO1 - MENU CONVERSIÓN DE MEDIDAS
def mostrar_menu():
    print("=== MENU DE CONVERSIÓN ===")
    print("Seleccione la conversión que desea realizar:")
    print("1. Metros a Centímetros")
    print("2. Metros a Kilómetros")
    print("3. Metros a Milímetros")
    print("4. Metros a Pulgadas")
def convertir_metros_a_centimetros(medida):
    resultado=medida * 100
    return resultado
def convertir_metros_a_kilometros(medida):
    resultado=medida / 1000
    return resultado
def convertir_metros_a_milimetros(medida):
    resultado=medida * 1000
    return resultado
def convertir_metros_a_pulgadas(medida):
    resultado=medida * 39.3701
    return resultado    
mostrar_menu()
opcion = input("Ingrese el número de la conversión que desea realizar: ")
medida = float(input("Ingrese la medida a convertir en metros (m): "))
print("=== RESULTADO DE CONVERSIÓN ===")
if opcion == '1':
    print(f"{medida} metros son {convertir_metros_a_centimetros(medida):.2f} centímetros.")
elif opcion == '2':
    print(f"{medida} metros son {convertir_metros_a_kilometros(medida):.4f} kilómetros.")
elif opcion == '3':
    print(f"{medida} metros son {convertir_metros_a_milimetros(medida):.2f} milímetros.")
elif opcion == '4':
    print(f"{medida} metros son {convertir_metros_a_pulgadas(medida):.2f} pulgadas.")
else:
    print("Opción no válida.")

# %%
#Ejercico2 - Menú de calificaciones
def mostrar_menu_calificaciones():
    print("=== MENU DE CALIFICACIONES ===")
    print("Seleccione la opción que desea realizar:")
    print("1. Calcular el promedio de tres calificaciones")
    print("2. Determinar si un estudiante aprobó o reprobó")
    print("3. Mostrar la nota mayor")
    print("4. Moastrar la nota menor")
    print("5. Salir")
def calcular_promedio(calificacion1, calificacion2, calificacion3):
    promedio = (calificacion1 + calificacion2 + calificacion3) / 3
    return promedio
def aprobacion(calificacion1, calificacion2, calificacion3):
    promedio = calcular_promedio(calificacion1, calificacion2, calificacion3)
    if promedio>=70:
        return "Aprobado"
    else:
        return "Reprobado"
def nota_mayor(calificacion1, calificacion2, calificacion3):
    if calificacion1>calificacion2 and calificacion1>calificacion2:
        return calificacion1
    elif calificacion2>calificacion1 and calificacion2>calificacion3:
        return calificacion2
    else:
        return calificacion3
def nota_menor(calificacion1, calificacion2, calificacion3):
    if calificacion1>calificacion2 and calificacion1>calificacion2:
        return calificacion2
    elif calificacion2>calificacion1 and calificacion3>calificacion1:
        return calificacion1
    else: 
        calificacion3
mostrar_menu_calificaciones()
opcion=input("Ingrese el número de la opción que desea realizar: ")
if opcion=="5":
    print("Saliendo del programa...")
else:
    calificacion1=float(input("Ingrese la primera calificación: "))
    calificacion2=float(input("Ingrese la segunda calificación: "))
    calificacion3=float(input("Ingrese la tercera calificación: "))
    if opcion=="1":
        print(f"El promedio de las calificaciones es: {calcular_promedio(calificacion1, calificacion2, calificacion3):.2f}")
    elif opcion=="2":
        print(f"El estudiante está: {aprobacion(calificacion1, calificacion2, calificacion3)}")
    elif opcion=="3":
        print(f"La nota mayor es: {nota_mayor(calificacion1, calificacion2, calificacion3)}")
    elif opcion=="4":
        print(f"La nota menor es: {nota_menor(calificacion1, calificacion2, calificacion3)}")
    else:
        print("Opción no válida.")
print("Fin del programa.")

# %%
