from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from src.auth.security import decodificar_token
from src.config.database import get_db
from src.models.usuario import Usuario


bearer_scheme = HTTPBearer() #formato en el que se recibira el token


def obtener_usuario_actual(
    credenciales: HTTPAuthorizationCredentials = Depends(bearer_scheme), #aqui se obtienen las credenciales
    db: Session = Depends(get_db) 
):
    token = credenciales.credentials
    payload = decodificar_token(token) #aqui se usa la funcion de decodificar para leer el token

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"} 
        )

    id_usuario = payload.get("sub") #si la validacion ocurre de manera exitosa se asigna este valor a la payload

    if id_usuario is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="El token no contiene un usuario válido",
            headers={"WWW-Authenticate": "Bearer"} 
        )

    usuario = (
        db.query(Usuario)
        .filter(Usuario.id_usuario == int(id_usuario))
        .first()
    )

    if usuario is None or not usuario.activo:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario inexistente o inactivo",
            headers={"WWW-Authenticate": "Bearer"}
        )

    return usuario #para concluir se verifican los valores dentro de payload para saber si es un usuario valido