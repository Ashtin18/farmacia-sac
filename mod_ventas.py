# ===============================================
# MÓDULO 3: VENTAS - FARMACIA SAC
# ===============================================

from mod_productos import mostrar_productos
from datetime import datetime

def realizar_venta(productos, precios, stock):
    total = 0
    seguir = "s"
    
    # Listas para guardar el detalle de la venta
    productos_vendidos = []
    cantidades_vendidas = []
    precios_unitarios = []
    subtotales = []
    
    while seguir.lower() == "s":
        mostrar_productos(productos, precios, stock)
        indice = int(input("Seleccione producto: ")) - 1
        
        if 0 <= indice < len(productos):
            cantidad = int(input("Cantidad: "))
            if cantidad <= stock[indice]:
                subtotal = precios[indice] * cantidad
                total += subtotal
                stock[indice] -= cantidad
                
                # Guardar detalles de la venta
                productos_vendidos.append(productos[indice])
                cantidades_vendidas.append(cantidad)
                precios_unitarios.append(precios[indice])
                subtotales.append(subtotal)
                
                print(f"Venta registrada. Subtotal: S/{subtotal:.2f}\n")
            else:
                print("Stock insuficiente.\n")
        else:
            print("Producto no válido.\n")
            
        seguir = input("¿Desea agregar otro producto? (s/n): ")
    
    # Mostrar comprobante de pago si hubo ventas
    if len(productos_vendidos) > 0:
        print("\n" + "="*50)
        print("           COMPROBANTE DE PAGO")
        print("            FARMACIA SAC")
        print("="*50)
        print(f"Fecha: {datetime.now()}")
        print("-"*50)
        print(f"{'PRODUCTO':<20} {'CANT':<6} {'P.UNIT':<10} {'SUBTOTAL':<10}")
        print("-"*50)
        
        for i in range(len(productos_vendidos)):
            print(f"{productos_vendidos[i]:<20} {cantidades_vendidas[i]:<6} S/{precios_unitarios[i]:<9.2f} S/{subtotales[i]:<9.2f}")
        
        print("-"*50)
        print(f"{'TOTAL A PAGAR:':<37} S/{total:.2f}")
        print("="*50)
        print("      ¡Gracias por su compra!")
        print("="*50 + "\n")
    else:
        print("\nNo se realizaron ventas.\n")