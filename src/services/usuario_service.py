from sqlalchemy.orm import Session

from src.repositories import usuario_repository
from src.schemas.usuario_schema import (
    UsuarioCreate,
    UsuarioUpdate
)


def obtener_usuarios(db: Session):
    usuarios = usuario_repository.get_all(db)

    resultado = []

    for usuario in usuarios:
        resultado.append(
            {
                "id_usuario": usuario.id_usuario,
                "nombre": usuario.nombre,
                "correo": usuario.correo,
                "rol": usuario.rol,
                "id_area": usuario.id_area,
                "nombre_area": (
                    usuario.area.nombre_area
                    if usuario.area
                    else None
                ),
                "activo": usuario.activo,
                "es_anfitrion": usuario.es_anfitrion,
                "fecha_creacion": usuario.fecha_creacion
            }
        )

    return resultado


def obtener_usuario_por_id(
    db: Session,
    id_usuario: int
):
    usuario = usuario_repository.get_by_id(
        db,
        id_usuario
    )

    if usuario is None:
        return None

    return {
        "id_usuario": usuario.id_usuario,
        "nombre": usuario.nombre,
        "correo": usuario.correo,
        "rol": usuario.rol,
        "id_area": usuario.id_area,
        "nombre_area": (
            usuario.area.nombre_area
            if usuario.area
            else None
        ),
        "activo": usuario.activo,
        "es_anfitrion": usuario.es_anfitrion,
        "fecha_creacion": usuario.fecha_creacion
    }


def obtener_anfitriones(db: Session):
    usuarios = usuario_repository.get_anfitriones(db)

    return [
        {
            "id_usuario": usuario.id_usuario,
            "nombre": usuario.nombre,
            "id_area": usuario.id_area
        }
        for usuario in usuarios
    ]


def crear_usuario(
    db: Session,
    usuario: UsuarioCreate
):
    return usuario_repository.create(
        db,
        usuario
    )


def actualizar_usuario(
    db: Session,
    id_usuario: int,
    usuario: UsuarioUpdate
):
    return usuario_repository.update(
        db,
        id_usuario,
        usuario
    )