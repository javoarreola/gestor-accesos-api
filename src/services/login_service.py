from sqlalchemy.orm import Session

from src.auth.security import crear_token_acceso
from src.repositories import login_repository
from src.schemas.login_schema import LoginRequest


def autenticar_usuario(
    db: Session,
    credenciales: LoginRequest
):
    usuario = login_repository.obtener_usuario_por_correo(
        db,
        credenciales.correo
    )

    if usuario is None:
        return None

    if not usuario.activo:
        return None

    # Comparación temporal.
    # Se reemplazará por verificación de hash.
    if usuario.password_hash != credenciales.password:
        return None

    token = crear_token_acceso(
        id_usuario=usuario.id_usuario,
        correo=usuario.correo,
        rol=usuario.rol
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "id_usuario": usuario.id_usuario,
        "nombre": usuario.nombre,
        "correo": usuario.correo,
        "rol": usuario.rol
    }