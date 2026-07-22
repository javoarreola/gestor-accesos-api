#Constantes de los roles disponibles en el sistema.
ADMINISTRADOR = "Administrador"
GUARDIA = "Guardia"
RECEPCION = "Recepción"

# Grupos de permisos frecuentes
SOLO_ADMIN = [
    ADMINISTRADOR
]

PERSONAL_OPERATIVO = [
    ADMINISTRADOR,
    GUARDIA,
    RECEPCION
]

ADMIN_GUARDIA = [
    ADMINISTRADOR,
    GUARDIA
]