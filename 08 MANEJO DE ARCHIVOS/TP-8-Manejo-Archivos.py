productos = []

try:
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:  # evita lineas vacias
                nombre, precio, cantidad = linea.split(",")
                producto = {
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad),
                }
                productos.append(producto)
                print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
except FileNotFoundError:
    print("El archivo productos.txt no existe. Se crea uno nuevo")

# Paso 3: agregar productos desde wl teclado
nuevo_nombre = input("\nIngrese el nombre del nuevo producto: ")
nuevo_precio = float(input("Ingrese el precio del producto: "))
nueva_cantidad = int(input("Ingrese la cantidad del producto: "))

nuevo_producto = {
    "nombre": nuevo_nombre,
    "precio": nuevo_precio,
    "cantidad": nueva_cantidad,
}

productos.append(nuevo_producto)

# Paso 4 y 6: guardar los productos actualizados
with open("productos.txt", "w") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("\nProducto agregado y archivo actualizado.")

# Paso 5: buscar producto por nombre
buscar_nombre = input("\nIngrese el nombre del producto a buscar: ")
encontrado = False
for p in productos:
    if p["nombre"].lower() == buscar_nombre.lower():
        print(
            f"Producto encontrado: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}"
        )
        encontrado = True
        break

if not encontrado:
    print("Producto no encontrado")
