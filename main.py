# ===============================================
# PROGRAMA PRINCIPAL - SISTEMA DE FARMACIA SAC
# ===============================================

from mod_login import iniciar_sesion
from mod_productos import agregar_producto, modificar_precio, mostrar_productos
from mod_inventario import mostrar_inventario_bajo
from mod_ventas import realizar_venta


# --- Datos centralizados del sistema ---
productos = ["Paracetamol", "Ibuprofeno", "Amoxicilina"]
precios = [2.5, 3.0, 5.5]
stock = [10, 8, 6]


def mostrar_menu(rol):
    """
    Muestra el menú principal del sistema según el rol del usuario.
    - Admin: acceso completo
    - Usuario: solo ventas y consultas
    """
    print("\n" + "="*40)
    print("   SISTEMA DE GESTIÓN - FARMACIA SAC")
    print(f"   ROL: {rol.upper()}")
    print("="*40)
    print("1. Registrar venta")
    
    if rol == "admin":
        print("2. Agregar producto")
        print("3. Modificar precio")
        print("4. Ver stock bajo")
    
    print("5. Ver todos los productos")
    print("6. Salir")
    print("="*40)


def main():
    """
    Función principal que controla el flujo del sistema.
    """
    print("\n*** BIENVENIDO AL SISTEMA DE FARMACIA SAC ***\n")
    
    # Validar inicio de sesión y obtener rol
    rol = iniciar_sesion()
    
    if rol:
        opcion = 0
        
        while opcion != 6:
            mostrar_menu(rol)
            
            try:
                opcion = int(input("\nSeleccione una opción: "))
                
                if opcion == 1:
                    realizar_venta(productos, precios, stock)
                    
                elif opcion == 2:
                    if rol == "admin":
                        agregar_producto(productos, precios, stock)
                    else:
                        print("\n⚠ Acceso denegado. Esta opción es solo para administradores.\n")
                        
                elif opcion == 3:
                    if rol == "admin":
                        modificar_precio(productos, precios, stock)
                    else:
                        print("\n⚠ Acceso denegado. Esta opción es solo para administradores.\n")
                        
                elif opcion == 4:
                    if rol == "admin":
                        mostrar_inventario_bajo(productos, stock)
                    else:
                        print("\n⚠ Acceso denegado. Esta opción es solo para administradores.\n")
                        
                elif opcion == 5:
                    mostrar_productos(productos, precios, stock)
                    
                elif opcion == 6:
                    print("\n¡Gracias por usar el sistema! Hasta pronto.\n")
                    
                else:
                    print("\n⚠ Opción inválida. Por favor, seleccione una opción válida.\n")
            
            except ValueError:
                print("\n⚠ Error: Debe ingresar un número válido.\n")
                opcion = 0
    else:
        print("\n❌ Acceso denegado. Intente más tarde.\n")


if __name__ == "__main__":
    main()


