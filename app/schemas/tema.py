from pydantic import BaseModel
from uuid import UUID


class TemaCreate(BaseModel):
    nombre: str
    materia: str
    grado: int
    orden_logico: int | None = None


class TemaUpdate(BaseModel):
    nombre: str | None = None
    materia: str | None = None
    grado: int | None = None
    orden_logico: int | None = None
    activo: bool | None = None


class TemaOut(BaseModel):
    id_tema: UUID
    nombre: str
    materia: str
    grado: int
    orden_logico: int | None
    activo: bool

    class Config:
        orm_mode = True