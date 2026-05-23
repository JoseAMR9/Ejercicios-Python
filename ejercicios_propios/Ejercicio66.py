import os
def clear():
    os.system("cls")
def pause():
    input("\nPresione ENTER para continuar...")

inventario = {
    "Laptop": {"precio": 3500, "stock": 5},
    "Mouse": {"precio": 80, "stock": 10}
}

def ver_productos(inventario):
    if len(inventario) == 0:
        print("No hay productos registrados")
        return

    print("\nPRODUCTOS DISPONIBLES: ")
    for producto, datos in inventario.items():
        print(f"{producto} | Precio: {datos['precio']} | Stock: {datos['stock']}")

def agregar_producto(inventario):
    nombre = input("\nNombre: ")
    if nombre in inventario:
        print("\nEl producto ya existe")
        return

    try:
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
        if precio < 0 or stock < 0:
            raise ValueError
        
    except ValueError:
        print("\nDatos invalidos")
        return
    
    inventario[nombre] = {"precio": precio, "stock": stock}

def comprar_producto(inventario):
    if len(inventario) == 0:
        print("No hay productos registrados")
        return

    nombre = input("\nNombre del producto: ")
    if nombre not in inventario:
        print("\nEl producto no existe")
        return

    try:
        cantidad = int(input("Cantidad: "))
        if cantidad < 0:
            raise ValueError("\nCantidad invalida")
        
    except ValueError:
        print("\nCantidad invalida")
        return
    
    if inventario[nombre]["stock"] < cantidad:
        print("\nStock insuficiente")
        return

    inventario[nombre]["stock"] -= cantidad
    total = inventario[nombre]["precio"] * cantidad

    print(f"\nTotal a pagar: {total}")

def mostrar_mas_caro(inventario):
    if len(inventario) == 0:
        print("No hay productos registrados")
        return
    
    nombre = ""
    precio = 0
    for producto in inventario:
        if inventario[producto]["precio"] > precio:
            nombre = producto
            precio = inventario[producto]["precio"]
    
    print(f"\nProducto mas caro: {nombre} - {precio}")

def mostrar_sin_stock(inventario):
    if len(inventario) == 0:
        print("No hay productos registrados")
        return

    tienen_stock = True

    for producto in inventario:
        if inventario[producto]["stock"] == 0:
            print(producto)
            tienen_stock = False

    if tienen_stock == True:
        print("\nTodos los productos tienen stock")

def actualizar_precio(inventario):
    if len(inventario) == 0:
        print("\nNo hay productos registrados")
        return

    nombre = input("\nIngrese el producto: ")

    if nombre not in inventario:
        print("\nEl producto no existe")
        return

    try:
        nuevo_precio = float(input("Ingrese el nuevo precio: "))
        if nuevo_precio < 0:
            raise ValueError("\nCantidad invalida")
    except ValueError as e:
        print(f"\n{e}")
        return

    inventario[nombre]["precio"] = nuevo_precio

def eliminar_producto(inventario):
    if len(inventario) == 0:
        print("\nNo hay productos registrados")
        return
    
    nombre_eliminar = input("\nIngrese el nombre del producto a eliminar: ")
    if nombre_eliminar not in inventario:
        print("\nEl producto no existe")
        return
    
    del inventario[nombre_eliminar]
    print("\nProducto eliminado exitosamente")

def ordenar_por_precio(inventario):
    if len(inventario) == 0:
        print("\nNo hay productos registrados")
        return

    productos_ordenados = sorted(
        inventario.items(),
        key=lambda producto: producto[1]["precio"],
        reverse=True
    )

    print("\nPRODUCTOS ORDENADOS POR PRECIO:\n")

    for nombre, datos in productos_ordenados:
        print(f"{nombre} | Precio: {datos['precio']} | Stock: {datos['stock']}")

def valor_total(inventario):
    if len(inventario) == 0:
        print("\nNo hay productos registrados")
        return

    value = 0

    for producto in inventario:
        value += inventario[producto]["precio"] * inventario[producto]["stock"]
    print(f"\nValor total del inventario es: {value}")

while True:
    clear()
    print("1.- Ver productos")
    print("2.- Agregar producto")
    print("3.- Comprar producto")
    print("4.- Mostrar producto mas caro")
    print("5.- Mostrar productos sin stock")
    print("6.- Actualizar el precio de un producto")
    print("7.- Eliminar producto")
    print("8.- Ordenar inventario")
    print("9.- Valor total del inventario")
    print("0.- Salir")

    try:
        opcion = int(input("\nElija una opcion: "))
    except ValueError:
        print("\nERROR")
        pause()
        continue
    
    match(opcion):
        case 1:
            clear()
            ver_productos(inventario)
            pause()
        case 2:
            clear()
            agregar_producto(inventario)
            pause()
        case 3:
            clear()
            comprar_producto(inventario)
            pause()
        case 4:
            clear()
            mostrar_mas_caro(inventario)
            pause()
        case 5:
            clear()
            mostrar_sin_stock(inventario)
            pause()
        case 6:
            clear()
            actualizar_precio(inventario)
            pause()
        case 7:
            clear()
            ver_productos(inventario)
            eliminar_producto(inventario)
            pause()
        case 8:
            clear()
            ordenar_por_precio(inventario)
            pause()
        case 9:
            clear()
            valor_total(inventario)
            pause()
        case 0:
            break
