import os
from datetime import datetime, timedelta, timezone
from typing import Any

import jwt
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES", "60"))


if not SECRET_KEY:
    raise RuntimeError(
        "La variable JWT_SECRET_KEY no está configurada en el archivo .env"
    )


def crear_token_acceso(
    id_usuario: int,
    correo: str,
    rol: str
) -> str:
    fecha_actual = datetime.now(timezone.utc)
    fecha_expiracion = fecha_actual + timedelta(
        minutes=EXPIRE_MINUTES
    )

    payload = {
        "sub": str(id_usuario),
        "correo": correo,
        "rol": rol,
        "iat": fecha_actual,
        "exp": fecha_expiracion
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


def decodificar_token(token: str) -> dict[str, Any] | None:
    try:
        return jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

    except jwt.ExpiredSignatureError:
        return None

    except jwt.InvalidTokenError:
        return None