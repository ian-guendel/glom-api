from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class EstudianteCreate(BaseModel):
    grado: int


class EstudianteUpdate(BaseModel):
    grado: int | None = None
    activo: bool | None = None


class EstudianteOut(BaseModel):
    id_estudiante: UUID
    grado: int
    activo: bool
    fecha_alta: datetime

    class Config:
        orm_mode = True