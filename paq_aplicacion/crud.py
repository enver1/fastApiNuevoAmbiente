from sqlalchemy.orm import Session
from paq_dominio.genPersona import genPersona
from paq_dominio.sgiPerfilEsquema import PerfilForm
from paq_dominio.sgiPerfil import sgiPerfil

def get_genPersona(db: Session, skip: int = 0, limit: int = 100, ):
    return db.query(genPersona).offset(skip).limit(limit).all()

#*********** PERFIL ***********
#crear perfil
def crear_perfil(db: Session, perfil: PerfilForm):
     obj = sgiPerfil(nombre=perfil.nombre, descrpcion=perfil.descripcion)
     db.add(obj)
     db.commit()
     db.flush(obj)
     return obj
#findAll
def get_sgiPerfil(db: Session, skip: int = 0, limit: int = 100, ):
    return db.query(sgiPerfil).offset(skip).limit(limit).all()