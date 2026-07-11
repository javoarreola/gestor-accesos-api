from sqlalchemy.orm import Session

from src.repositories import registro_acceso_repository
from src.schemas.registro_acceso_schema import (
    RegistroAccesoCreate,
    RegistroAccesoUpdate
)


def obtener_registros(db: Session):
    return registro_acceso_repository.get_all(db)


def obtener_registro_por_id(
    db: Session,
    id_registro: int
):
    return registro_acceso_repository.get_by_id(
        db,
        id_registro
    )


def crear_registro(
    db: Session,
    registro: RegistroAccesoCreate
):
    return registro_acceso_repository.create(
        db,
        registro
    )


def actualizar_registro(
    db: Session,
    id_registro: int,
    registro: RegistroAccesoUpdate
):
    return registro_acceso_repository.update(
        db,
        id_registro,
        registro
    )


def eliminar_registro(
    db: Session,
    id_registro: int
):
    return registro_acceso_repository.delete(
        db,
        id_registro
    )