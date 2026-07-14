from sqlalchemy import Column, Integer, String
from src.config.database import Base


''' Modelo que representa la tabla Empresas de la base de datos '''
class Empresa(Base):
    __tablename__ = "Empresas"

    id_empresa = Column(
        "ID_Empresa", 
        Integer, 
        primary_key=True, 
        index=True
        )
    
    nombre_empresa = Column(
        "Nombre_Empresa", 
        String(150), 
        nullable=False, 
        unique=True
        )
    
