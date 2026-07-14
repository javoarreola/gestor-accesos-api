from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.config.database import get_db
from src.schemas.login_schema import (
    LoginRequest,
    TokenResponse
)
from src.services import login_service


router = APIRouter(
    prefix="/login",
    tags=["Autenticación"]
)


@router.post("/", response_model=TokenResponse)
def iniciar_sesion(
    credenciales: LoginRequest,
    db: Session = Depends(get_db)
):
    resultado = login_service.autenticar_usuario(
        db,
        credenciales
    )

    if resultado is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"}
        )

    return resultado