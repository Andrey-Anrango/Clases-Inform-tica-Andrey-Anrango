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
