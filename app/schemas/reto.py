from pydantic import BaseModel
from uuid import UUID


class RetoCreate(BaseModel):
    id_tema: UUID
    nivel: int


class RetoUpdate(BaseModel):
    nivel: int | None = None
    activo: bool | None = None


class RetoOut(BaseModel):
    id_reto: UUID
    id_tema: UUID
    nivel: int
    activo: bool

    class Config:
        orm_mode = True