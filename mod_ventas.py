# ===============================================
# MÓDULO 3: VENTAS - FARMACIA SAC
# ===============================================

from mod_productos import mostrar_productos


def realizar_venta(productos, precios, stock):
    """
    Permite registrar una venta de uno o varios productos.
    Actualiza el stock automáticamente tras cada venta.
    """
    total = 0
    seguir = "s"
    
    while seguir.lower() == "s":
        mostrar_productos(productos, precios, stock)
        pos = int(input("Seleccione producto: ")) - 1
        
        if 0 <= pos < len(productos):
            cantidad = int(input("Cantidad: "))
            if cantidad <= stock[pos]:
                subtotal = precios[pos] * cantidad
                total += subtotal
                stock[pos] -= cantidad
                print(f"Venta registrada. Subtotal: S/{subtotal:.2f}\n")
            else:
                print("Stock insuficiente.\n")
        else:
            print("Producto no válido.\n")
            
        seguir = input("¿Desea agregar otro producto? (s/n): ")
    
    print(f"TOTAL DE LA VENTA: S/{total:.2f}\n")


# --- Datos iniciales de prueba ---
if __name__ == "__main__":
    productos = ["Paracetamol", "Ibuprofeno", "Amoxicilina"]
    precios = [2.5, 3.0, 5.5]
    stock = [10, 8, 6]
    
    print("=== MÓDULO DE VENTAS - PRUEBA ===")
    print("(Para prueba interactiva, ejecute realizar_venta)")
    mostrar_productos(productos, precios, stock)
    # realizar_venta(productos, precios, stock)  # Descomentar para prueba interactiva