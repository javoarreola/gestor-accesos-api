from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.config.database import get_db
from src.schemas.registro_acceso_schema import (
    RegistroAccesoCreate,
    RegistroAccesoUpdate,
    RegistroAccesoResponse
)
from src.services import registro_acceso_service

from src.dependencies.auth_dependencies import obtener_usuario_actual

router = APIRouter(
    prefix="/registros-accesos",
    tags=["Registro de Accesos"],
    dependencies=[Depends(obtener_usuario_actual)]
)


@router.get("/", response_model=List[RegistroAccesoResponse])
def obtener_registros(
    db: Session = Depends(get_db)
):
    return registro_acceso_service.obtener_registros(db)


@router.get("/{id_registro}", response_model=RegistroAccesoResponse)
def obtener_registro(
    id_registro: int,
    db: Session = Depends(get_db)
):
    registro = registro_acceso_service.obtener_registro_por_id(
        db,
        id_registro
    )

    if registro is None:
        raise HTTPException(
            status_code=404,
            detail="Registro no encontrado"
        )

    return registro


@router.post("/", response_model=RegistroAccesoResponse)
def crear_registro(
    registro: RegistroAccesoCreate,
    db: Session = Depends(get_db)
):
    return registro_acceso_service.crear_registro(
        db,
        registro
    )


@router.put("/{id_registro}", response_model=RegistroAccesoResponse)
def actualizar_registro(
    id_registro: int,
    registro: RegistroAccesoUpdate,
    db: Session = Depends(get_db)
):
    registro_actualizado = (
        registro_acceso_service.actualizar_registro(
            db,
            id_registro,
            registro
        )
    )

    if registro_actualizado is None:
        raise HTTPException(
            status_code=404,
            detail="Registro no encontrado"
        )

    return registro_actualizado


@router.delete("/{id_registro}")
def eliminar_registro(
    id_registro: int,
    db: Session = Depends(get_db)
):
    registro_eliminado = (
        registro_acceso_service.eliminar_registro(
            db,
            id_registro
        )
    )

    if registro_eliminado is None:
        raise HTTPException(
            status_code=404,
            detail="Registro no encontrado"
        )

    return {
        "message": "Registro eliminado correctamente"
    }