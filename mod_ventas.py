# ===============================================
# MÓDULO 3: VENTAS - FARMACIA SAC
# ===============================================

from mod_productos import mostrar_productos

def realizar_venta(productos, precios, stock):
    total = 0
    seguir = "s"
    
    while seguir.lower() == "s":
        mostrar_productos(productos, precios, stock)
        indice = int(input("Seleccione producto: ")) - 1
        
        if 0 <= indice < len(productos):
            cantidad = int(input("Cantidad: "))
            if cantidad <= stock[indice]:
                subtotal = precios[indice] * cantidad
                total += subtotal
                stock[indice] -= cantidad
                print(f"Venta registrada. Subtotal: S/{subtotal:.2f}\n")
            else:
                print("Stock insuficiente.\n")
        else:
            print("Producto no válido.\n")
            
        seguir = input("¿Desea agregar otro producto? (s/n): ")
    
    print(f"TOTAL DE LA VENTA: S/{total:.2f}\n")