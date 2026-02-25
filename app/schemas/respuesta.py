from pydantic import BaseModel
from uuid import UUID


class RespuestaCreate(BaseModel):
    id_pregunta: UUID
    texto: str
    correcta: bool = False


class RespuestaUpdate(BaseModel):
    texto: str | None = None
    correcta: bool | None = None


class RespuestaOut(BaseModel):
    id_respuesta: UUID
    id_pregunta: UUID
    texto: str
    correcta: bool

    class Config:
        orm_mode = True