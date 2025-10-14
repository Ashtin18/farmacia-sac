# ===============================================
# MÓDULO 4: INVENTARIO - FARMACIA SAC
# ===============================================


def mostrar_inventario_bajo(productos, stock, limite=5):
    """
    Muestra productos con stock bajo (menor al límite especificado).
    Por defecto, el límite es 5 unidades.
    """
    print("\n=== ALERTA DE STOCK BAJO ===")
    hay_productos_bajos = False
    
    for i in range(len(productos)):
        if stock[i] < limite:
            print(f"{productos[i]} -> Stock actual: {stock[i]}")
            hay_productos_bajos = True
    
    if not hay_productos_bajos:
        print("No hay productos con stock bajo.")
    
    print("=============================\n")


# --- Datos iniciales de prueba ---
if __name__ == "__main__":
    productos = ["Paracetamol", "Ibuprofeno", "Amoxicilina", "Aspirina"]
    stock = [10, 3, 6, 2]
    
    print("=== MÓDULO DE INVENTARIO - PRUEBA ===")
    mostrar_inventario_bajo(productos, stock)