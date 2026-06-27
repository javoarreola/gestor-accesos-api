from sqlalchemy.orm import Session

from src.repositories import area_repository
from src.schemas.area_schema import AreaCreate, AreaUpdate


def obtener_areas(db: Session):
    return area_repository.get_all(db)


def obtener_area_por_id(db: Session, id_area: int):
    return area_repository.get_by_id(db, id_area)


def crear_area(db: Session, area: AreaCreate):
    return area_repository.create(db, area)


def actualizar_area(db: Session, id_area: int, area: AreaUpdate):
    return area_repository.update(db, id_area, area)


def eliminar_area(db: Session, id_area: int):
    return area_repository.delete(db, id_area)