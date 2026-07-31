from typing import Optional

from datetime import datetime

from sqlalchemy.orm import Session

from src.models.visitante import Visitante
from src.schemas.visitante_schema import (
    VisitanteCreate,
    VisitanteUpdate
)

def normalizar_texto(valor: str) -> str:
    return " ".join(
        palabra.capitalize()
        for palabra in valor.strip().split()
    )

def get_all(
    db: Session,
    nombre: Optional[str] = None
):
    consulta = db.query(Visitante)

    if nombre:
        termino = f"%{nombre.strip()}%"

        consulta = consulta.filter(
            (
                Visitante.nombre.ilike(termino)
            )
            |
            (
                Visitante.apellido.ilike(termino)
            )
        )

    return consulta.all()


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
        nombre=normalizar_texto(visitante.nombre),
        apellido=normalizar_texto(visitante.apellido),
        identificacion=visitante.identificacion.strip().upper(),
        telefono=visitante.telefono.strip(),
        fecha_registro=datetime.now()
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

    visitante_db.nombre = normalizar_texto(
    visitante.nombre
    )

    visitante_db.apellido = normalizar_texto(
        visitante.apellido
    )

    visitante_db.identificacion = (
        visitante.identificacion.strip().upper()
    )

    visitante_db.telefono = visitante.telefono.strip()

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