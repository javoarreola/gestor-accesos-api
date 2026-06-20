from fastapi import FastAPI
from sqlalchemy import text

from src.config.database import engine

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "Gestor de Accesos API"
    }


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