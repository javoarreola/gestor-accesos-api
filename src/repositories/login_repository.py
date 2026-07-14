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
    )