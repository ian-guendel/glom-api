from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Literal


class IntentoCreate(BaseModel):
    id_estudiante: UUID
    id_reto: UUID
    id_tema: UUID
    nivel: int
    numero_intento: int
    resultado: Literal["correcto", "incorrecto", "abandono"]
    tiempo_segundos: int | None = None


class IntentoOut(BaseModel):
    id_intento: UUID
    id_estudiante: UUID
    id_reto: UUID
    id_tema: UUID
    nivel: int
    numero_intento: int
    resultado: str
    tiempo_segundos: int | None
    timestamp: datetime

    class Config:
        orm_mode = True