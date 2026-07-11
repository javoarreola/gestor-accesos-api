from sqlalchemy.orm import Session

from src.models.visitante import Visitante
from src.schemas.visitante_schema import (
    VisitanteCreate,
    VisitanteUpdate
)


def get_all(db: Session):
    return db.query(Visitante).all()


def get_by_id(db: Session, id_visitante: int):
    return (
        db.query(Visitante)
        .filter(
            Visitante.id_visitante == id_visitante
        )
        .first()
    )


def create(
    db: Session,
    visitante: VisitanteCreate
):

    nuevo_visitante = Visitante(
        id_empresa=visitante.id_empresa,
        nombre=visitante.nombre,
        apellido=visitante.apellido,
        identificacion=visitante.identificacion,
        telefono=visitante.telefono
    )

    db.add(nuevo_visitante)
    db.commit()
    db.refresh(nuevo_visitante)

    return nuevo_visitante


def update(
    db: Session,
    id_visitante: int,
    visitante: VisitanteUpdate
):

    visitante_db = get_by_id(
        db,
        id_visitante
    )

    if visitante_db is None:
        return None

    visitante_db.id_empresa = visitante.id_empresa
    visitante_db.nombre = visitante.nombre
    visitante_db.apellido = visitante.apellido
    visitante_db.identificacion = visitante.identificacion
    visitante_db.telefono = visitante.telefono

    db.commit()
    db.refresh(visitante_db)

    return visitante_db


def delete(
    db: Session,
    id_visitante: int
):

    visitante_db = get_by_id(
        db,
        id_visitante
    )

    if visitante_db is None:
        return None

    db.delete(visitante_db)
    db.commit()

    return visitante_db