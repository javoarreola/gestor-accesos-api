from datetime import datetime

from pydantic import BaseModel

#dtos de visitantes
class VisitanteBase(BaseModel):
    id_empresa: int
    nombre: str
    apellido: str
    identificacion: str
    telefono: str


class VisitanteCreate(VisitanteBase):
    pass


class VisitanteUpdate(VisitanteBase):
    pass


class VisitanteResponse(VisitanteBase):
    id_visitante: int
    fecha_registro: datetime

    class Config:
        from_attributes = True