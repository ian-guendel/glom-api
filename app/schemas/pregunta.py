from pydantic import BaseModel
from uuid import UUID


class PreguntaCreate(BaseModel):
    id_reto: UUID
    enunciado: str


class PreguntaUpdate(BaseModel):
    enunciado: str | None = None


class PreguntaOut(BaseModel):
    id_pregunta: UUID
    id_reto: UUID
    enunciado: str

    class Config:
        orm_mode = True