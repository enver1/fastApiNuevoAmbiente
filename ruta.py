from paq_infraestructura.Conexion import Base, engine, localSession
from fastapi import APIRouter, Depends
from paq_aplicacion import servicios
from sqlalchemy.orm import Session
from paq_dominio.sgiPerfilEsquema import PerfilForm
from paq_aplicacion import crud

Base.metadata.create_all(bind=engine)


def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()

#genPersona
#obtener 100 registro de genPersona
ruta_genPersona = APIRouter()
@ruta_genPersona.get("/genPersona")
def obtenet_genPersona(db: Session = Depends(get_db)):
    return servicios.get_genPersona_limite(db=db)    
#--------------------- PERFIL -----------------
#crear
ruta_sgiPerfil = APIRouter()
@ruta_sgiPerfil.post("/sgiPerfil")
def ingresar_perfil(perfil: PerfilForm, db: Session = Depends(get_db)):
    return crud.crear_perfil(db=db,perfil=perfil)
#findAll
@ruta_sgiPerfil.get("/sgiPerfil")
def obtenet_todos_perfiles(db: Session = Depends(get_db)):
    return crud.get_sgiPerfil(db=db)  

