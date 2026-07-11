from sqlalchemy.orm import Session

from src.repositories import visitante_repository
from src.schemas.visitante_schema import (
    VisitanteCreate,
    VisitanteUpdate
)


def obtener_visitantes(db: Session):
    return visitante_repository.get_all(db)


def obtener_visitante_por_id(
    db: Session,
    id_visitante: int
):
    return visitante_repository.get_by_id(
        db,
        id_visitante
    )


def crear_visitante(
    db: Session,
    visitante: VisitanteCreate
):
    return visitante_repository.create(
        db,
        visitante
    )


def actualizar_visitante(
    db: Session,
    id_visitante: int,
    visitante: VisitanteUpdate
):
    return visitante_repository.update(
        db,
        id_visitante,
        visitante
    )


def eliminar_visitante(
    db: Session,
    id_visitante: int
):
    return visitante_repository.delete(
        db,
        id_visitante
    )