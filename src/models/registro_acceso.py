from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String
)
from sqlalchemy.orm import relationship

from src.config.database import Base


'''  Modelo que registra las entradas y salidas de los visitantes '''
class RegistroAcceso(Base):
    __tablename__ = "Registro_Accesos"

    id_registro = Column(
        "ID_Registro",
        Integer,
        primary_key=True,
        index=True
    )

    id_visitante = Column(
        "ID_Visitante",
        Integer,
        ForeignKey("Visitantes.ID_Visitante"),
        nullable=False
    )

    id_area = Column(
        "ID_Area",
        Integer,
        ForeignKey("Areas.ID_Area"),
        nullable=False
    )

    id_usuario = Column(
        "ID_Usuario",
        Integer,
        ForeignKey("Usuarios.ID_Usuario"),
        nullable=False
    )

    anfitrion = Column(
        "Anfitrion",
        String(150),
        nullable=False
    )

    motivo_visita = Column(
        "Motivo_Visita",
        String(255),
        nullable=False
    )

    fecha_hora_entrada = Column(
        "Fecha_Hora_Entrada",
        DateTime,
        nullable=False
    )

    fecha_hora_salida = Column(
        "Fecha_Hora_Salida",
        DateTime,
        nullable=True
    )

    estatus = Column(
        "Estatus",
        String(50),
        nullable=False
    )

    visitante = relationship("Visitante")
    area = relationship("Area")
    usuario = relationship("Usuario")