from datetime import datetime

from pydantic import BaseModel
#dtos de usuarios

class UsuarioBase(BaseModel):
    nombre: str
    correo: str
    rol: str


class UsuarioCreate(UsuarioBase):
    password_hash: str
    es_anfitrion: bool = False

class UsuarioUpdate(UsuarioBase):
    password_hash: str
    activo: bool
    es_anfitrion: bool

class UsuarioResponse(UsuarioBase):
    id_usuario: int
    activo: bool
    es_anfitrion: bool
    fecha_creacion: datetime

    class Config:
        from_attributes = True

class UsuarioAnfitrionResponse(BaseModel):
    id_usuario: int
    nombre: str

    class Config:
        from_attributes = True