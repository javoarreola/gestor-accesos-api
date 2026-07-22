from typing import List

from fastapi import Depends, HTTPException, status

from src.dependencies.auth_dependencies import obtener_usuario_actual
from src.models.usuario import Usuario


def permitir_roles(roles_permitidos: List[str]):
    
    """
    Crea una dependencia que valida si el usuario autenticado
    tiene uno de los roles autorizados.
    """

    def validar_rol(
        usuario_actual: Usuario = Depends(obtener_usuario_actual)
    ):
       
        """
        Verifica que el rol del usuario se encuentre autorizado.
        """

        if usuario_actual.rol not in roles_permitidos:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No tiene permisos para realizar esta acción"
            )

        return usuario_actual

    return validar_rol