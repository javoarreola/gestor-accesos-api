from sqlalchemy.orm import Session

from src.models.registro_acceso import RegistroAcceso
from src.schemas.registro_acceso_schema import (
    RegistroAccesoCreate,
    RegistroAccesoUpdate
)


def get_all(db: Session):
    return db.query(RegistroAcceso).all() #devuelve todos los registros


def get_by_id(
    db: Session,
    id_registro: int
):
    return (
        db.query(RegistroAcceso)
        .filter(
            RegistroAcceso.id_registro == id_registro
        )
        .first() #busca registros por medio de id
    )


def create(
    db: Session,
    registro: RegistroAccesoCreate
):

    nuevo_registro = RegistroAcceso(
        id_visitante=registro.id_visitante,
        id_area=registro.id_area,
        id_usuario=registro.id_usuario,
        anfitrion=registro.anfitrion,
        motivo_visita=registro.motivo_visita
    )

    db.add(nuevo_registro)
    db.commit()
    db.refresh(nuevo_registro)

    return nuevo_registro #crea un nuevo registro en la base de datos


def update(
    db: Session,
    id_registro: int,
    registro: RegistroAccesoUpdate
):

    registro_db = get_by_id(
        db,
        id_registro
    )

    if registro_db is None:
        return None

    registro_db.id_visitante = registro.id_visitante
    registro_db.id_area = registro.id_area
    registro_db.id_usuario = registro.id_usuario
    registro_db.anfitrion = registro.anfitrion
    registro_db.motivo_visita = registro.motivo_visita
    registro_db.fecha_hora_entrada = registro.fecha_hora_entrada
    registro_db.fecha_hora_salida = registro.fecha_hora_salida
    registro_db.estatus = registro.estatus

    db.commit()
    db.refresh(registro_db)

    return registro_db #actualiza un registro existente
 

def delete(
    db: Session,
    id_registro: int
):

    registro_db = get_by_id(
        db,
        id_registro
    )

    if registro_db is None:
        return None

    db.delete(registro_db)
    db.commit()

    return registro_db #elimina un registro existente