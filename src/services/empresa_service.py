from sqlalchemy.orm import Session
from src.repositories import empresa_repository
from src.schemas.empresa_schema import EmpresaCreate, EmpresaUpdate


def obtener_empresas(db: Session):
    return empresa_repository.get_all(db)


def obtener_empresa_por_id(
    db: Session, 
    id_empresa: int
    ):

    return empresa_repository.get_by_id(
        db, 
        id_empresa
    )


def crear_empresa(
    db: Session, 
    empresa: EmpresaCreate
    ):

    return empresa_repository.create(
        db, empresa
    )


def actualizar_empresa(
    db: Session, 
    id_empresa: int, 
    empresa: EmpresaUpdate
    ):

    return empresa_repository.update(
    db, 
    id_empresa, 
    empresa
    )


def eliminar_empresa(
    db: Session, 
    id_empresa: int
    ):

    return empresa_repository.delete(
    db, id_empresa
    )