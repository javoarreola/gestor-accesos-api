import os
import smtplib

from email.message import EmailMessage
from dotenv import load_dotenv


load_dotenv()


SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_FROM = os.getenv("SMTP_FROM", SMTP_USER)


def notificar_llegada_visitante(
    destinatario: str,
    nombre_anfitrion: str,
    nombre_visitante: str,
    motivo_visita: str,
    fecha_hora_entrada: str
) -> bool:
    """
    Envía una notificación al anfitrión cuando llega un visitante.
    """

    if not SMTP_SERVER or not SMTP_USER or not SMTP_PASSWORD:
        print(
            "No se pudo enviar la notificación: "
            "faltan variables de configuración SMTP."
        )
        return False

    mensaje = EmailMessage()

    mensaje["From"] = SMTP_FROM
    mensaje["To"] = destinatario
    mensaje["Subject"] = "Llegada de visitante"

    contenido = f"""
Hola, {nombre_anfitrion}:

El visitante {nombre_visitante} ha llegado a las instalaciones.

Motivo de la visita: {motivo_visita}
Fecha y hora de entrada: {fecha_hora_entrada}

Favor de presentarse o comunicarse con recepción.

Este mensaje fue generado automáticamente por el Sistema de Gestión de Accesos.
""".strip()

    mensaje.set_content(contenido)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as servidor:
            servidor.starttls()
            servidor.login(
                SMTP_USER,
                SMTP_PASSWORD
            )
            servidor.send_message(mensaje)

        print(
            f"Notificación enviada correctamente a: {destinatario}"
        )

        return True

    except Exception as error:
        print(
            f"Error al enviar la notificación a {destinatario}: {error}"
        )

        return False