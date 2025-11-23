# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)

# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero = input("Escriba un numero: ")

cantidad = len(str(abs(numero)))
print("Cantidad de dígitos:", cantidad)

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

inicio = min(a, b) + 1
fin = max(a, b)

suma = 0
for i in range(inicio, fin):
    suma += i

print("La suma es:", suma)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

total = 0
while True:
    num = int(input("Ingrese un numero (0 para terminar): "))
    if num == 0:
        break
    total += num

print("Total acumulado:", total)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random

secreto = random.randint(0, 9)
intentos = 0

while True:
    num = int(input("Adivine el número (0-9): "))
    intentos += 1

    if num == secreto:
        print("¡Correcto! El número era", secreto)
        print("Intentos:", intentos)
        break

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
numero_positivo = int(input("Ingrese un numero entero positivo: "))

suma = 0
for i in range(numero_positivo + 1):
    suma += i

print("La suma es:", suma)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cantidad = 100

pares = impares = positivos = negativos = 0

for i in range(cantidad):
    num = int(input(f"Ingrese el número {i+1}: "))

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

cantidad = 100
suma = 0

for i in range(cantidad):
    num = int(input(f"Ingrese el numero {i+1}: "))
    suma += num

media = suma / cantidad
print("La media es:", media)

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = input("Ingrese un numero: ")
invertido = num[::-1]
print("Numero invertido:", invertido)
