# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas = {"Banana": 1200, "Ananá": 2500, "Melón": 3000, "Uva": 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800
# Actualizar precios
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.
frutas = list(precios_frutas.keys())
print(frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
telefonos = {}

# Cargo 5 contactos
for i in range(5):
    nombre = input(f"Ingrese nombre del contacto {i+1}: ")
    numero = input(f"Ingrese numero de {nombre}: ")
    telefonos[nombre] = numero

# Consulto numero
nombre_buscar = input("Ingrese el nombre a consultar: ")
if nombre_buscar in telefonos:
    print(f"Número de {nombre_buscar}: {telefonos[nombre_buscar]}")
else:
    print("Contacto no encontrado")

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.
frase = input("Ingrese una frase: ")

# Palabras unicas usando set
palabras = frase.split()
unicas = set(palabras)
print("Palabras unicas:", unicas)

conteo = {}
for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1
print("Conteo de palabras:", conteo)

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.
alumnos = {}

for i in range(3):
    nombre = input(f"Ingrese nombre del alumno {i+1}: ")
    notas = tuple(float(input(f"Nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

# Promedio de cada alumno
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre} tiene promedio {promedio:.2f}")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)
parcial1 = {1, 2, 3, 4}
parcial2 = {3, 4, 5, 6}

# Aprobados ambos parciales
ambos = parcial1 & parcial2
print("Aprobados en ambos:", ambos)

# Aprobados solo en uno
solo_uno = parcial1 ^ parcial2
print("Aprobados solo en uno:", solo_uno)

# Aprobados en al menos uno
al_menos_uno = parcial1 | parcial2
print("Aprobados al menos en uno:", al_menos_uno)

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

productos = {"Manzanas": 50, "Bananas": 30, "Naranjas": 20}

while True:
    accion = input(
        "Quiere consultar/agregar producto? (consultar/agregar/salir): "
    ).lower()

    if accion == "salir":
        break
    elif accion == "consultar":
        nombre = input("Ingrese el nombre del producto: ")
        if nombre in productos:
            print(f"Stock de {nombre}: {productos[nombre]}")
        else:
            print("Producto no encontrado.")
    elif accion == "agregar":
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad a agregar: "))
        if nombre in productos:
            productos[nombre] += cantidad
            print(f"Nuevo stock de {nombre}: {productos[nombre]}")
        else:
            productos[nombre] = cantidad
            print(f"Producto {nombre} agregado con stock {cantidad}.")
    else:
        print("Opción no valida.")

print("Stock final:", productos)

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Ejemplo:

agenda = {
    ("Lunes", "10:00"): "Matematica",
    ("Martes", "14:00"): "Programacion",
    ("Miercoles", "09:00"): "Fsica",
}

dia = input("Ingrese el dia a consultar: ")
hora = input("Ingrese la hora a consultar (HH:MM): ")

evento = agenda.get((dia, hora))
if evento:
    print(f"En {dia} a las {hora} hay: {evento}")
else:
    print("No hay actividad programada en ese horario ")

# Permití consultar qué actividad hay en cierto día y hora.
# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores

paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
}

capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

print("Diccionario invertido:", capitales_paises)
