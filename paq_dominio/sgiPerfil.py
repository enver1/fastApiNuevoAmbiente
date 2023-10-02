from sqlalchemy import Column, Integer, String, ForeignKey
from paq_infraestructura.Conexion import Base
from sqlalchemy.orm import relationship

class sgiPerfil(Base):
    __tablename__ = 'sgiPerfil'
    idSgiPerfil = Column( Integer, primary_key=True)
    nombre = Column(String(100))     
    descrpcion = Column(String(100))          
