from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.respuesta import RespuestaCreate, RespuestaUpdate, RespuestaOut
from app.crud import respuesta as crud

router = APIRouter(prefix="/respuestas", tags=["Respuestas"])


@router.post("/", response_model=RespuestaOut)
def create_respuesta(data: RespuestaCreate, db: Session = Depends(get_db)):
    return crud.create_respuesta(db, data)


@router.get("/", response_model=list[RespuestaOut])
def list_respuestas(db: Session = Depends(get_db)):
    return crud.get_respuestas(db)


@router.get("/{respuesta_id}", response_model=RespuestaOut)
def get_respuesta(respuesta_id, db: Session = Depends(get_db)):
    obj = crud.get_respuesta(db, respuesta_id)
    if not obj:
        raise HTTPException(404, "Respuesta no encontrada")
    return obj


@router.put("/{respuesta_id}", response_model=RespuestaOut)
def update_respuesta(
    respuesta_id,
    data: RespuestaUpdate,
    db: Session = Depends(get_db),
):
    obj = crud.update_respuesta(db, respuesta_id, data)
    if not obj:
        raise HTTPException(404, "Respuesta no encontrada")
    return obj


@router.delete("/{respuesta_id}")
def delete_respuesta(respuesta_id, db: Session = Depends(get_db)):
    obj = crud.delete_respuesta(db, respuesta_id)
    if not obj:
        raise HTTPException(404, "Respuesta no encontrada")
    return {"ok": True}