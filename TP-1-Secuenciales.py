# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

print('Hola Mundo!')

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.


nombre = input('Ingrese su nombre: ')
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = input('Ingrese su edad: ')
residencia = input('Ingrese su lugar de residencia: ')
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

radio = int(input('Por favor, ingrese el radio del circulo: '))
perimetro = radio*2
area = radio**3.14
print(f"El area del circulo es {area} y su perimetro es {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

segundos = int(input('Ingrese los segundos: '))
print(f"Los segundos equivalen a {segundos//3600} horas")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

numero = int(input("Por favor, ingrese un numero: "))
print(f"La tabla del numero es: "
     f"{numero} x 1 = {numero*1}\n"
     f"{numero} x 2 = {numero*2}\n"
     f"{numero} x 3 = {numero*3}\n"
     f"{numero} x 4 = {numero*4}\n"
     f" {numero} x 5 = {numero*5}\n"
     f" {numero} x 6 = {numero*6}\n"
     f" {numero} x 7 = {numero*7}\n"
     f" {numero} x8 = {numero*8}\n"
     f" {numero} x 9 = {numero*9}\n"
     f"{numero} x 10 = {numero*10}") 

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero1 = int(input('Por favor, ingrese numero mayor a 0: '))
numero2 = int(input('Por favor, ingrese otro numero mayor a 0: '))
print(f'Suma de ambos = {numero1+numero2}, resta = {numero1 - numero2}, division = {numero1/numero2}, multiplicacion = {numero1 * numero2}')

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo:

altura = int(input('Por favor, ingrese su altura en metros: '))
peso = int(input('Ingrese su peso en kg: '))
print(f'Su indice de masa corporal es: {peso/altura**2}')

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

tempCelcius = int(input('Por favor, ingrese la temperatura en Celsius: '))
print(f'La temperatura en Farenheit es: {9/5*tempCelcius+32}')

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('ingrese el segundo numero: '))
num3 = int(input('Ingrese el tercer numero: '))
print(f'El promedio de los tres numeros es: {num1+num2+num3/3}')