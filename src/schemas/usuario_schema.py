from datetime import datetime

from pydantic import BaseModel
#dtos de usuarios

class UsuarioBase(BaseModel):
    nombre: str
    correo: str
    rol: str


class UsuarioCreate(UsuarioBase):
    password_hash: str


class UsuarioUpdate(UsuarioBase):
    password_hash: str
    activo: bool


class UsuarioResponse(UsuarioBase):
    id_usuario: int
    activo: bool
    fecha_creacion: datetime

    class Config:
        from_attributes = True