from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.config.database import get_db
from src.schemas.visitante_schema import (
    VisitanteCreate,
    VisitanteUpdate,
    VisitanteResponse
)
from src.services import visitante_service

router = APIRouter(
    prefix="/visitantes",
    tags=["Visitantes"]
)


@router.get("/", response_model=List[VisitanteResponse])
def obtener_visitantes(db: Session = Depends(get_db)):
    return visitante_service.obtener_visitantes(db)


@router.get("/{id_visitante}", response_model=VisitanteResponse)
def obtener_visitante(
    id_visitante: int,
    db: Session = Depends(get_db)
):
    visitante = visitante_service.obtener_visitante_por_id(
        db,
        id_visitante
    )

    if visitante is None:
        raise HTTPException(
            status_code=404,
            detail="Visitante no encontrado"
        )

    return visitante


@router.post("/", response_model=VisitanteResponse)
def crear_visitante(
    visitante: VisitanteCreate,
    db: Session = Depends(get_db)
):
    return visitante_service.crear_visitante(
        db,
        visitante
    )


@router.put("/{id_visitante}", response_model=VisitanteResponse)
def actualizar_visitante(
    id_visitante: int,
    visitante: VisitanteUpdate,
    db: Session = Depends(get_db)
):
    visitante_actualizado = visitante_service.actualizar_visitante(
        db,
        id_visitante,
        visitante
    )

    if visitante_actualizado is None:
        raise HTTPException(
            status_code=404,
            detail="Visitante no encontrado"
        )

    return visitante_actualizado


@router.delete("/{id_visitante}")
def eliminar_visitante(
    id_visitante: int,
    db: Session = Depends(get_db)
):
    visitante_eliminado = visitante_service.eliminar_visitante(
        db,
        id_visitante
    )

    if visitante_eliminado is None:
        raise HTTPException(
            status_code=404,
            detail="Visitante no encontrado"
        )

    return {
        "message": "Visitante eliminado correctamente"
    }