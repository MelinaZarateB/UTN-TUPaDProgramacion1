# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

nota = int(input("Ingrese el valor de su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input("Por favor, ingrese un numero: "))
if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a mayor")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

# contraseña = input("ingrese una contraseña: ")
# if len(contraseña) >= 8 and len(contraseña) <= 14:
#     print("Ha ingresado una contraseña correcta")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
# siguiente:
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if media > mediana > moda:
    print("Hay sesgo positivo")
elif media < mediana < moda:
    print("Hay sesgo negativo")
else:
    print("No hay sesgo")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

frase = input("Ingrese una frase o palabra: ")

texto = frase[-1]
if texto.lower() in "aeiou":
    print(f"{frase}!")
else:
    print(frase)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.

nombre = input("Ingrese su nombre ")

opcion = int(
    input(
        f"Ingrese la opcion numerica que desee: \n"
        f" 1. Si quiere su nombre en mayúsculas. Por ejemplo: {nombre.lower()} \n"
        f" 2. Si quiere su nombre en minúsculas. Por ejemplo: {nombre.upper()} \n"
        f" 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: {nombre.title()} \n"
    )
)
if opcion == 1:
    print(nombre.lower())
elif opcion == 2:
    print(nombre.upper())
elif opcion == 3:
    print(nombre)
else:
    pass

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# • Menor que 3: "Muy leve" (imperceptible).
# • Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# • Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# • Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# • Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# • Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = int(input("Ingrese la magnitud de un terremoto: "))

if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
else:
    print("Extremo")

# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año :
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("Ingrese el hemisferio en el que se encuentra: ")
mes = input("Ingrese el mes del año: ")
dia = int(input("Ingrese el dia: "))

if hemisferio.lower() == "sur":
    if (
        (mes.lower() == "diciembre" and dia >= 21)
        or (mes.lower() == "enero" or mes.lower() == "febrero")
        or (mes.lower() == "marzo" and dia <= 20)
    ):
        print("Verano")
    elif (
        (mes.lower() == "marzo" and dia >= 21)
        or (mes.lower() == "abril" or mes.lower() == "mayo")
        or (mes.lower() == "junio" and dia <= 20)
    ):
        print("Otoño")
    elif (
        (mes.lower() == "junio" and dia >= 21)
        or (mes.lower() == "julio" or mes.lower() == "agosto")
        or (mes.lower() == "septiembre" and dia <= 20)
    ):
        print("Invierno")
    else:
        print("Primavera")

if hemisferio.lower() == "norte":
    if (
        (mes.lower() == "diciembre" and dia >= 21)
        or (mes.lower() == "enero" or mes.lower() == "febrero")
        or (mes.lower() == "marzo" and dia <= 20)
    ):
        print("Invierno")
    elif (
        (mes.lower() == "marzo" and dia >= 21)
        or (mes.lower() == "abril" or mes.lower() == "mayo")
        or (mes.lower() == "junio" and dia <= 20)
    ):
        print("Primavera")
    elif (
        (mes.lower() == "junio" and dia >= 21)
        or (mes.lower() == "julio" or mes.lower() == "agosto")
        or (mes.lower() == "septiembre" and dia <= 20)
    ):
        print("Verano")
    else:
        print("Otoño")
