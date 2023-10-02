from sqlalchemy.orm import Session
from paq_aplicacion import crud

def get_genPersona_limite(db: Session, skip: int = 0, limit: int = 100):
    return crud.get_genPersona(db, skip, limit);