# ===============================================
# MÓDULO 1: INICIO DE SESIÓN - FARMACIA SAC
# ===============================================

def iniciar_sesion():
    """
    Valida las credenciales del usuario.
    Permite 3 intentos antes de bloquear el acceso.
    Retorna el rol del usuario o None si falla el acceso.
    
    Roles:
    - 'admin': Acceso completo al sistema
    - 'usuario': Acceso limitado (solo ventas y consultas)
    """
    # Usuarios, contraseñas y roles del sistema
    usuarios = ["admin", "ashtin", "usuario"]
    contraseñas = ["1234", "abcd", "0000"]
    roles = ["admin", "usuario", "usuario"]
    
    print("=== INICIO DE SESIÓN ===")
    intentos = 3
    
    while intentos > 0:
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")
        
        # Validar credenciales
        if usuario in usuarios:
            indice = usuarios.index(usuario)
            if contraseña == contraseñas[indice]:
                rol = roles[indice]
                print(f"\nInicio de sesión exitoso. Bienvenido, {usuario} [{rol.upper()}]")
                return rol  
        
        intentos -= 1
        print("Credenciales incorrectas. Intentos restantes:", intentos, "\n")

    print("Demasiados intentos. Saliendo del sistema.")
    return None 

