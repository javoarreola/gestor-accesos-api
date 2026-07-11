from sqlalchemy.orm import Session

from src.models.usuario import Usuario
from src.schemas.usuario_schema import (
    UsuarioCreate,
    UsuarioUpdate
)


def get_all(db: Session):
    return db.query(Usuario).all()


def get_by_id(db: Session, id_usuario: int):
    return (
        db.query(Usuario)
        .filter(Usuario.id_usuario == id_usuario)
        .first()
    )


def create(db: Session, usuario: UsuarioCreate):
    nuevo_usuario = Usuario(
        nombre=usuario.nombre,
        correo=usuario.correo,
        rol=usuario.rol,
        password_hash=usuario.password_hash,
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return nuevo_usuario


def update(
    db: Session,
    id_usuario: int,
    usuario: UsuarioUpdate
):
    usuario_db = get_by_id(db, id_usuario)

    if usuario_db is None:
        return None

    usuario_db.nombre = usuario.nombre
    usuario_db.correo = usuario.correo
    usuario_db.rol = usuario.rol
    usuario_db.password_hash = usuario.password_hash
    usuario_db.activo = usuario.activo

    db.commit()
    db.refresh(usuario_db)

    return usuario_db


def delete(db: Session, id_usuario: int):
    usuario_db = get_by_id(db, id_usuario)

    if usuario_db is None:
        return None

    db.delete(usuario_db)
    db.commit()

    return usuario_db