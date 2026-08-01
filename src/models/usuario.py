from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship

from src.config.database import Base


''' Modelo que almacena la información de los usuarios del sistema '''
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
    es_anfitrion = Column(
        "Es_Anfitrion",
        Boolean,
        nullable=False
        )
    id_area = Column(
        "ID_Area",
        Integer,
        ForeignKey("Areas.ID_Area"),
        nullable=False
    )
    fecha_creacion = Column(
        "Fecha_Creacion", 
        DateTime, 
        nullable=False
        )
    area = relationship(
        "Area",
        back_populates="usuarios"
    )