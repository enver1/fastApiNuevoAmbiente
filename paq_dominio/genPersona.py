from sqlalchemy import Column, Integer, String, ForeignKey
from paq_infraestructura.Conexion import Base
from sqlalchemy.orm import relationship

class genPersona(Base):
    __tablename__ = 'genPersona'
    idGenPersona = Column( Integer, primary_key=True)
    idGenDivPolitica = Column(Integer)
    idGenTipoSangre = Column(Integer, ForeignKey('genTipoSangre.idGenTipoSangre'), primary_key=True, index=True, )    
    idGenEtnia = Column( Integer)
    idGenDivPoliticaLn = Column( Integer)
    idGenEstaCivil = Column(String(100))     
    apellido1 = Column(String(100))     
    apellido2 = Column(String(100))
    nombre1 = Column(String(100))
    nombre2 = Column(String(100))
    apenom = Column(String(100))
    fechaNacimiento = Column(String(100))
    fechaDefuncion = Column(String(100))
    sexo = Column(String(100))
    codigoDactilar = Column(String(100))
    usuario = Column( Integer)
    fecha = Column(String(100))
    ip = Column(String(100))

class genTipoSangre(Base):
    __tablename__ = 'genTipoSangre'
    idGenTipoSangre = Column(Integer, primary_key=True)

class genEstaCivil(Base):
    __tablename__ = 'genEstaCivil'
    idGenEstaCivil = Column(Integer, primary_key=True)





