from pydantic import BaseModel

class PerfilForm(BaseModel):
    nombre: str
    descripcion: str

class PerfilId(PerfilForm):
    id: int
    