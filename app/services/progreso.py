from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from app.models.progreso import ProgresoTemaEstudiante
from app.models.intento import Intento


def recalcular_progreso(
    db: Session,
    id_estudiante,
    id_tema,
):
    """
    Recalcula el progreso cognitivo de un estudiante en un tema
    a partir de los intentos registrados.
    """

    # Traer todos los intentos del estudiante en el tema
    intentos = (
        db.query(Intento)
        .filter(
            Intento.id_estudiante == id_estudiante,
            Intento.id_tema == id_tema,
        )
        .all()
    )

    if not intentos:
        return

    intentos_totales = len(intentos)
    aciertos = sum(1 for i in intentos if i.resultado == "correcto")
    errores = sum(1 for i in intentos if i.resultado == "incorrecto")

    tasa_error = errores / intentos_totales
    porcentaje_dominio = aciertos / intentos_totales

    # Por ahora: último nivel jugado
    nivel_actual = max(i.nivel for i in intentos)

    progreso = (
        db.query(ProgresoTemaEstudiante)
        .filter_by(
            id_estudiante=id_estudiante,
            id_tema=id_tema,
        )
        .first()
    )

    if not progreso:
        progreso = ProgresoTemaEstudiante(
            id_estudiante=id_estudiante,
            id_tema=id_tema,
        )
        db.add(progreso)

    progreso.intentos_totales = intentos_totales
    progreso.aciertos_totales = aciertos
    progreso.errores_totales = errores
    progreso.tasa_error = tasa_error
    progreso.porcentaje_dominio = porcentaje_dominio
    progreso.nivel_actual = nivel_actual
    progreso.ultima_actualizacion = func.now()

    db.commit()