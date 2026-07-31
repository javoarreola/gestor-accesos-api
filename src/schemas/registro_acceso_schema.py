from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Datos comunes para crear un registro
class RegistroAccesoCreate(BaseModel):
    id_visitante: int
    id_area: int
    id_usuario: int
    motivo_visita: str


# Datos requeridos para actualizar un registro completo
class RegistroAccesoUpdate(BaseModel):
    id_visitante: int
    id_area: int
    id_usuario: int
    motivo_visita: str
    fecha_hora_entrada: datetime
    fecha_hora_salida: Optional[datetime] = None
    estatus: str


# Datos para registrar la salida
class RegistroSalida(BaseModel):
    fecha_hora_salida: Optional[datetime] = None


# Respuesta del registro de acceso
class RegistroAccesoResponse(BaseModel):
    id_registro: int
    id_visitante: int
    id_area: int
    id_usuario: int
    anfitrion: str
    motivo_visita: str
    fecha_hora_entrada: datetime
    fecha_hora_salida: Optional[datetime] = None
    estatus: str

    class Config:
        from_attributes = True


# Respuesta utilizada por el historial
class RegistroAccesoHistorialResponse(BaseModel):
    id_registro: int
    visitante: str
    area: str
    anfitrion: str
    motivo_visita: str
    fecha_hora_entrada: datetime
    fecha_hora_salida: Optional[datetime] = None
    estatus: str