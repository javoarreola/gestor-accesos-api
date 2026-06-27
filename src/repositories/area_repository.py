from sqlalchemy.orm import Session

from src.models.area import Area
from src.schemas.area_schema import AreaCreate, AreaUpdate


def get_all(db: Session):
    return db.query(Area).all()


def get_by_id(db: Session, id_area: int):
    return db.query(Area).filter(Area.id_area == id_area).first()


def create(db: Session, area: AreaCreate):
    nueva_area = Area(
        nombre_area=area.nombre_area
    )

    db.add(nueva_area)
    db.commit()
    db.refresh(nueva_area)

    return nueva_area


def update(db: Session, id_area: int, area: AreaUpdate):
    area_db = get_by_id(db, id_area)

    if area_db is None:
        return None

    area_db.nombre_area = area.nombre_area

    db.commit()
    db.refresh(area_db)

    return area_db


def delete(db: Session, id_area: int):
    area_db = get_by_id(db, id_area)

    if area_db is None:
        return None

    db.delete(area_db)
    db.commit()

    return area_db