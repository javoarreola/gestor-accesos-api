from sqlalchemy import Column, Integer, String, Boolean, DateTime

from src.config.database import Base


class Usuario(Base):
    __tablename__ = "Usuarios"

    id_usuario = Column(
        "ID_Usuario", 
        Integer, 
        primary_key=True, 
        index=True
        )
    nombre = Column(
        "Nombre", 
        String(100), 
        nullable=False
        )
    correo = Column(
        "Correo", 
        String(150), 
        nullable=False, 
        unique=True
        )
    rol = Column(
        "Rol", 
        String(50), 
        nullable=False
        )
    password_hash = Column(
        "Password_Hash", 
        String(255), 
        nullable=False
        )
    activo = Column(
        "Activo", 
        Boolean, 
        nullable=False
        )
    fecha_creacion = Column(
        "Fecha_Creacion", 
        DateTime, 
        nullable=False
        )