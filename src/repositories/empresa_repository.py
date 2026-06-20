from sqlalchemy.orm import Session
from src.models.empresa import Empresa
from src.schemas.empresa_schema import EmpresaCreate, EmpresaUpdate


def get_all(db: Session):
    return db.query(Empresa).all()


def get_by_id(db: Session, id_empresa: int):
    return db.query(Empresa).filter(Empresa.id_empresa == id_empresa).first()


def create(db: Session, empresa: EmpresaCreate):
    nueva_empresa = Empresa(
        nombre_empresa=empresa.nombre_empresa
    )

    db.add(nueva_empresa)
    db.commit()
    db.refresh(nueva_empresa)

    return nueva_empresa


def update(db: Session, id_empresa: int, empresa: EmpresaUpdate):
    empresa_db = get_by_id(db, id_empresa)

    if empresa_db is None:
        return None

    empresa_db.nombre_empresa = empresa.nombre_empresa

    db.commit()
    db.refresh(empresa_db)

    return empresa_db


def delete(db: Session, id_empresa: int):
    empresa_db = get_by_id(db, id_empresa)

    if empresa_db is None:
        return None

    db.delete(empresa_db)
    db.commit()

    return empresa_db