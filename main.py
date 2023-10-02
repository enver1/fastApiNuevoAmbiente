from fastapi import FastAPI
from ruta import ruta_genPersona, ruta_sgiPerfil
app = FastAPI()
app.include_router(ruta_genPersona)
app.include_router(ruta_sgiPerfil)