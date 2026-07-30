from fastapi import FastAPI
from sqlalchemy import text

from src.config.database import engine
from src.routers.empresa_router import router as empresa_router
from src.routers.area_router import router as area_router
from src.routers.usuario_router import router as usuario_router
from src.routers.visitante_router import router as visitante_router
from src.routers.registro_acceso_router import (
    router as registro_acceso_router
)
from src.routers.login_router import router as login_router
from fastapi.middleware.cors import CORSMiddleware


# Inicialización de la aplicación FastAPI.
app = FastAPI(
    title="Gestor de Accesos API",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://127.0.0.1",
        "http://localhost:80",
        "http://127.0.0.1:80"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registro de los módulos principales de la API.
app.include_router(empresa_router)
app.include_router(area_router)
app.include_router(usuario_router)
app.include_router(visitante_router)
app.include_router(registro_acceso_router)
app.include_router(login_router)


# Endpoint principal de bienvenida.
@app.get("/")
def root():
    return {
        "message": "Gestor de Accesos API"
    }


# Endpoint para comprobar la conexión con la base de datos.
@app.get("/test-db")
def test_db():

    with engine.connect() as connection:

        result = connection.execute(
            text("SELECT DB_NAME()")
        )

        database_name = result.scalar()

    return {
        "database": database_name,
        "status": "Conexión exitosa"
    }