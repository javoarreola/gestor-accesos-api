from sqlalchemy.orm import Session

from src.repositories import usuario_repository
from src.schemas.usuario_schema import (
    UsuarioCreate,
    UsuarioUpdate
)


def obtener_usuarios(db: Session):
    return usuario_repository.get_all(db)


def obtener_usuario_por_id(db: Session, id_usuario: int):
    return usuario_repository.get_by_id(db, id_usuario)


def crear_usuario(db: Session, usuario: UsuarioCreate):
    return usuario_repository.create(db, usuario)


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
