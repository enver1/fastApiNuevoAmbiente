from sqlalchemy import Column, Integer, String
from paq_infraestructura.Conexion import Base

class Estudiante(Base):
    __tablename__ = 'genPersona'
    idGenPersona = Column( Integer, primary_key=True)
    idGenDivPolitica = Column( Integer)
    idGenTipoSangre = Column( Integer)
    idGenEtnia = Column( Integer)
    idGenDivPoliticaLn = Column( Integer)
    idGenEstaCivil = Column( Integer)
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
