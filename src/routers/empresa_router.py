from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.config.database import get_db
from src.dependencies.auth_dependencies import obtener_usuario_actual
from src.schemas.empresa_schema import (
    EmpresaCreate, 
    EmpresaUpdate, 
    EmpresaResponse
)
from src.services import empresa_service




router = APIRouter(
    prefix="/empresas",
    tags=["Empresas"],
    dependencies=[Depends(obtener_usuario_actual)]
)


@router.get(
    "/",
    response_model=List[EmpresaResponse]
)
def obtener_empresas(
    db: Session = Depends(get_db),
):
    return empresa_service.obtener_empresas(db)


@router.get(
    "/{id_empresa}",
    response_model=EmpresaResponse
)
def obtener_empresa(
    id_empresa: int,
    db: Session = Depends(get_db)
):

    empresa = empresa_service.obtener_empresa_por_id(
        db,
        id_empresa
    )

    if empresa is None:
        raise HTTPException(
            status_code=404,
            detail="Empresa no encontrada"
        )

    return empresa


@router.post(
    "/",
    response_model=EmpresaResponse
)
def crear_empresa(
    empresa: EmpresaCreate,
    db: Session = Depends(get_db)
):
    return empresa_service.crear_empresa( #se llaman las funciones para crear una empresa
        db,
        empresa
    )


@router.put(
    "/{id_empresa}",
    response_model=EmpresaResponse
)
def actualizar_empresa(
    id_empresa: int,
    empresa: EmpresaUpdate,
    db: Session = Depends(get_db)
):

    empresa_actualizada = (
        empresa_service.actualizar_empresa(
            db,
            id_empresa,
            empresa
        )
    )

    if empresa_actualizada is None:
        raise HTTPException(
            status_code=404,
            detail="Empresa no encontrada"
        )

    return empresa_actualizada #se busca la empresa por medio de id, empresa update devuelve la estructura, luego se usara la funcion de actualizar empresa para realizar cambios


@router.delete("/{id_empresa}")
def eliminar_empresa(
    id_empresa: int,
    db: Session = Depends(get_db)
):

    empresa_eliminada = (
        empresa_service.eliminar_empresa(
            db,
            id_empresa
        )
    )

    if empresa_eliminada is None:
        raise HTTPException(
            status_code=404,
            detail="Empresa no encontrada"
        )

    return {
        "message": "Empresa eliminada correctamente"
    }