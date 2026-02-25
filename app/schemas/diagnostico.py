from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class DiagnosticoOut(BaseModel):
    id_diagnostico: UUID
    id_estudiante: UUID
    id_tema: UUID
    nivel_detectado: int | None
    fecha: datetime

    class Config:
        orm_mode = True