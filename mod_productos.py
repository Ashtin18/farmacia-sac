# ===============================================
# MÓDULO 2: GESTIÓN DE PRODUCTOS - FARMACIA SAC
# ===============================================

def mostrar_productos(productos, precios, stock):
    """
    Muestra todos los productos con sus precios y stock disponible.
    """
    print("\n=== LISTA DE PRODUCTOS ===")
    for i in range(len(productos)):
        print(f"{i + 1} - {productos[i]} | Precio: S/{precios[i]:.2f} | Stock: {stock[i]}")
    print("============================\n")

    
def agregar_producto(productos, precios, stock):
    """
    Permite agregar un nuevo producto al inventario.
    """
    print("\n=== AGREGAR PRODUCTO ===")
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Stock inicial: "))
    productos.append(nombre)
    precios.append(precio)
    stock.append(cantidad)
    print("Producto agregado correctamente.\n")


def modificar_precio(productos, precios, stock):
    """
    Permite modificar el precio de un producto existente.
    """
    mostrar_productos(productos, precios, stock)
    pos = int(input("Seleccione número de producto para modificar precio: ")) - 1
    if 0 <= pos < len(productos):
        nuevo_precio = float(input("Nuevo precio: "))
        precios[pos] = nuevo_precio
        print("Precio actualizado.\n")
    else:
        print("Opción inválida.\n")
