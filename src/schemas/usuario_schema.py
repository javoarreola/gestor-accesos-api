from datetime import datetime

from pydantic import BaseModel


class UsuarioBase(BaseModel):
    nombre: str
    correo: str
    rol: str
    id_area: int


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
    nombre_area: str | None = None

    class Config:
        from_attributes = True


class UsuarioAnfitrionResponse(BaseModel):
    id_usuario: int
    nombre: str
    id_area: int

    class Config:
        from_attributes = True