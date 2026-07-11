from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.config.database import Base


class Visitante(Base):
    __tablename__ = "Visitantes"

    id_visitante = Column(
        "ID_Visitante",
        Integer,
        primary_key=True,
        index=True
    )

    id_empresa = Column(
        "ID_Empresa",
        Integer,
        ForeignKey("Empresas.ID_Empresa"),
        nullable=False
    )

    nombre = Column(
        "Nombre",
        String(100),
        nullable=False
    )

    apellido = Column(
        "Apellido",
        String(100),
        nullable=False
    )

    identificacion = Column(
        "Identificacion",
        String(100),
        nullable=False
    )

    telefono = Column(
        "Telefono",
        String(20),
        nullable=False
    )

    fecha_registro = Column(
        "Fecha_Registro",
        DateTime,
        nullable=False
    )

    empresa = relationship("Empresa")