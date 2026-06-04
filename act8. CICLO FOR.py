numeros= [0, 1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)
#fin
notas =   [8, 7, 9, 10, 6]
suma=0
contador=0
for nota in notas:
    suma=suma+nota
    contador=contador+1
promedio=suma/contador
print(f"El promedio es: {promedio}")
# %%
language = "Python"
for letra in language:
    print(letra)
# %%
palabra = input("ingresa una palabra: ")
vocales = 0
consonantes=0
suma=0
for letra in palabra:
    if letra =="a" or letra =="A" or letra =="e" or letra =="E" or letra =="i" or letra =="I" or letra =="o" or letra =="O" or letra =="u" or letra =="U":
        vocales=vocales+1
    else:
        consonantes=consonantes+1
suma= consonantes+vocales
print (f"consonantes totales: {consonantes}")
print(f"vocales totales: {vocales}")
print(f"letras totales: {suma}")
# %%
it_companies = {"Facebook", "Facebook", "Google", "Apple", "Amazon"}
for company in it_companies:
    print(company)
# %%
asistentes= {"Ana", "Luis", "Maria", "Ana", "Carlos", "Luis"}
for estudiante in asistentes:
    print("certificado para: ", estudiante)

# %%
#ENCONTRAR NUMERO EN LISTA
lista= [1, 2, 3, 4, 5]
numbers= int(input("ingresa un numero: "))
for number in lista:
    if number == numbers:
        print("se encontro el numero")
        break
else: 
    print("no se encontro el numero")
# %%
#CEDULA
cedula= input("Ingrese su numero de cedula: ")
cedula_limpia= ""
for caracter in cedula:
    if caracter == "-" or caracter == " ":
        continue
    cedula_limpia = cedula_limpia + caracter
print(cedula_limpia)

