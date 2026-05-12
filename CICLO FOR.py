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
