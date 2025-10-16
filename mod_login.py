# ===============================================
# MÓDULO 1: INICIO DE SESIÓN - FARMACIA SAC
# ===============================================

def iniciar_sesion():
    """
    Valida las credenciales del usuario.
    Permite 3 intentos antes de bloquear el acceso.
    Los usuarios están definidos internamente en este módulo.
    """
    # Usuarios y contraseñas del sistema
    usuarios = ["admin", "ashtin", "usuario"]
    contraseñas = ["1234", "abcd", "0000"]
    
    print("=== INICIO DE SESIÓN ===")
    intentos = 3
    
    while intentos > 0:
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")
        
        # Validar credenciales de forma simplificada
        if usuario in usuarios:
            indice = usuarios.index(usuario)
            if contraseña == contraseñas[indice]:
                print("\nInicio de sesión exitoso. Bienvenido,", usuario)
                return True
        
        intentos -= 1
        print("Credenciales incorrectas. Intentos restantes:", intentos, "\n")

    print("Demasiados intentos. Saliendo del sistema.")
    return False

