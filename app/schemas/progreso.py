from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class ProgresoTemaEstudianteOut(BaseModel):
    id_estudiante: UUID
    id_tema: UUID
    nivel_actual: int | None
    intentos_totales: int | None
    aciertos_totales: int | None
    errores_totales: int | None
    tasa_error: float | None
    porcentaje_dominio: float | None
    ultima_actualizacion: datetime

    class Config:
        orm_mode = True