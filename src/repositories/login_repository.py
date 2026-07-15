from sqlalchemy.orm import Session

from src.models.usuario import Usuario


def obtener_usuario_por_correo(
    db: Session,
    correo: str
):
    return (
        db.query(Usuario)
        .filter(Usuario.correo == correo)
        .first()
    ) #funcion para buscar un usuario por medio de correo, se compara el que se haya ingresado con los disponibles en la base de datos