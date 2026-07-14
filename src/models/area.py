from sqlalchemy import Column, Integer, String

from src.config.database import Base


''' Modelo que registra las areas o departamentos que conforman la empresa '''
class Area(Base):
    __tablename__ = "Areas"

    id_area = Column(
        "ID_Area",
        Integer,
        primary_key=True,
        index=True
    )

    nombre_area = Column(
        "Nombre_Area",
        String(100),
        nullable=False,
        unique=True
    )