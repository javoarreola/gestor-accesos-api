from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from src.config.database import get_db
from src.schemas.area_schema import (
    AreaCreate,
    AreaUpdate,
    AreaResponse
)
from src.services import area_service

router = APIRouter(
    prefix="/areas",
    tags=["Áreas"]
)


@router.get("/", response_model=List[AreaResponse])
def obtener_areas(db: Session = Depends(get_db)):
    return area_service.obtener_areas(db)


@router.get("/{id_area}", response_model=AreaResponse)
def obtener_area(id_area: int, db: Session = Depends(get_db)):
    area = area_service.obtener_area_por_id(db, id_area)

    if area is None:
        raise HTTPException(status_code=404, detail="Área no encontrada")

    return area


@router.post("/", response_model=AreaResponse)
def crear_area(area: AreaCreate, db: Session = Depends(get_db)):
    return area_service.crear_area(db, area)


@router.put("/{id_area}", response_model=AreaResponse)
def actualizar_area(
    id_area: int,
    area: AreaUpdate,
    db: Session = Depends(get_db)
):
    area_actualizada = area_service.actualizar_area(db, id_area, area)

    if area_actualizada is None:
        raise HTTPException(status_code=404, detail="Área no encontrada")

    return area_actualizada


@router.delete("/{id_area}")
def eliminar_area(id_area: int, db: Session = Depends(get_db)):
    area_eliminada = area_service.eliminar_area(db, id_area)

    if area_eliminada is None:
        raise HTTPException(status_code=404, detail="Área no encontrada")

    return {
        "message": "Área eliminada correctamente"
    }