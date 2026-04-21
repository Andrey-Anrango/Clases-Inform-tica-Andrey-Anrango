string_varias_lineas = """
Andrey Anrango
Python Developer
"""
print(string_varias_lineas)
# %%
colegio="ISM_North"
longitud_colegio=len(colegio)
print("La longitud del nombre del colegio es:", longitud_colegio)
print(len("San Francisco de Quito"))
nombre="Andrey"
apellido="Anrango"
space= " "
nombre_completo = nombre + space + apellido
print("Mi nombre completo es:", nombre_completo)
print(nombre_completo*3)


print("python\nchallenge")
print("nombre\tSemana1\tSemana2\tSemana3")
print("Simbolo(\\)")
print(f"Mi nombre es: {nombre} y mi apellido es {apellido}")
# %%
palabra="Python"
a,b,c,d,e,f=palabra
print(palabra[2])
last_three=palabra[3:6]
print("Las últimas tres letras de la palabra 'Python' son:", last_three)
# %%
greeting = "Hello, World!"
print(greeting[::-1])
thn=palabra[2:3:6]
print(palabra[0:6:2])
challenge="thirty days of python" 
print(challenge.capitalize())
print(challenge.count("y"))
