from datetime import datetime
from typing import Optional

from pydantic import BaseModel

#DTOs de registro
class RegistroAccesoBase(BaseModel):
    id_visitante: int
    id_area: int
    id_usuario: int
    anfitrion: str
    motivo_visita: str


class RegistroAccesoCreate(RegistroAccesoBase):
    pass


class RegistroAccesoUpdate(RegistroAccesoBase):
    fecha_hora_entrada: datetime
    fecha_hora_salida: Optional[datetime] = None
    estatus: str


class RegistroSalida(BaseModel):
    fecha_hora_salida: Optional[datetime] = None


class RegistroAccesoResponse(RegistroAccesoBase):
    id_registro: int
    fecha_hora_entrada: datetime
    fecha_hora_salida: Optional[datetime] = None
    estatus: str

    class Config:
        from_attributes = True