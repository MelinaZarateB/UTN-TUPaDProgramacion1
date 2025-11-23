# 1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja

notas = [7.5, 8.2, 9.1, 6.4, 7.9, 8.8, 5.3, 9.5, 6.7, 8.0]

# Mostrar lista completa
for nota in notas:
    print(nota)

# Promedio
promedio = sum(notas) / len(notas)
print("Promedio:", promedio)

# Mayor y menor
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))


# 2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []
for i in range(5):
    prod = input("Ingrese un producto: ")
    productos.append(prod)

print("Productos ordenados:")
for p in sorted(productos):
    print(p)

eliminar = input("¿Que producto quiere eliminar?: ")

if eliminar in productos:
    productos.remove(eliminar)

print("Lista actualizada:")
for p in productos:
    print(p)


# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

import random

numeros = [random.randint(1, 100) for _ in range(15)]

pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("Cantidad de pares:", len(pares))
print("Cantidad de impares:", len(impares))


# 4) Dada una lista con valores repetidos:
# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.

lista = [1, 2, 2, 3, 4, 4, 4, 5]
sin_repetidos = []

for elem in lista:
    if elem not in sin_repetidos:
        sin_repetidos.append(elem)

print("Lista sin repetidos:")
for x in sin_repetidos:
    print(x)

# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

estudiantes = ["Ana", "Luis", "Carlos", "María", "Elena", "Juan", "Sofía", "Pablo"]

accion = input("Quiere agregar o eliminar un estudiante? (agregar/eliminar): ")

if accion == "agregar":
    nuevo = input("Nombre del estudiante: ")
    estudiantes.append(nuevo)

elif accion == "eliminar":
    borrar = input("Nombre a eliminar: ")
    if borrar in estudiantes:
        estudiantes.remove(borrar)

print("Lista final:")
for e in estudiantes:
    print(e)

# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
# último pasa a ser el primero).

lista = [10, 20, 30, 40, 50, 60, 70]

ultimo = lista[-1]

for i in range(len(lista) - 1, 0, -1):
    lista[i] = lista[i - 1]

lista[0] = ultimo

print(lista)
