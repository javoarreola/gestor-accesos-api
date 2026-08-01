from sqlalchemy.orm import Session

from src.repositories import registro_acceso_repository
from src.schemas.registro_acceso_schema import (
    RegistroAccesoCreate,
    RegistroAccesoUpdate
)
from src.services import (
    usuario_service,
    visitante_service,
    email_service
)


def obtener_registros(db: Session):
    registros = registro_acceso_repository.get_all(db)

    historial = []

    for registro in registros:
        nombre_visitante = (
            f"{registro.visitante.nombre} "
            f"{registro.visitante.apellido}"
        )

        historial.append(
    {
        "id_registro": registro.id_registro,
        "visitante": nombre_visitante,
        "area": registro.area.nombre_area,
        "anfitrion": registro.anfitrion,
        "motivo_visita": registro.motivo_visita,
        "fecha_hora_entrada": registro.fecha_hora_entrada,
        "fecha_hora_salida": registro.fecha_hora_salida,
        "estatus": registro.estatus
    }
)

    return historial


def obtener_registro_por_id(
    db: Session,
    id_registro: int
):
    return registro_acceso_repository.get_by_id(
        db,
        id_registro
    )


def crear_registro(
    db: Session,
    registro: RegistroAccesoCreate
):
    usuario = usuario_service.obtener_usuario_por_id(
        db,
        registro.id_usuario
    )

    if usuario is None:
        return None

    visitante = visitante_service.obtener_visitante_por_id(
        db,
        registro.id_visitante
    )

    if visitante is None:
        return None

    nuevo_registro = registro_acceso_repository.create(
        db,
        registro
    )

    if nuevo_registro is None:
        return None

    email_service.notificar_llegada_visitante(
        destinatario=usuario["correo"],
        nombre_anfitrion=usuario["nombre"],
        nombre_visitante=(
            f"{visitante.nombre} "
            f"{visitante.apellido}"
        ),
        motivo_visita=registro.motivo_visita,
        fecha_hora_entrada=str(
            nuevo_registro.fecha_hora_entrada
        )
    )

    return nuevo_registro


def actualizar_registro(
    db: Session,
    id_registro: int,
    registro: RegistroAccesoUpdate
):
    return registro_acceso_repository.update(
        db,
        id_registro,
        registro
    )


def eliminar_registro(
    db: Session,
    id_registro: int
):
    return registro_acceso_repository.delete(
        db,
        id_registro
    )

def registrar_salida(
    db: Session,
    id_registro: int
):
    return registro_acceso_repository.registrar_salida(
        db,
        id_registro
    )