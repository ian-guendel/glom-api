from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.pregunta import PreguntaCreate, PreguntaUpdate, PreguntaOut
from app.crud import pregunta as crud

router = APIRouter(prefix="/preguntas", tags=["Preguntas"])


@router.post("/", response_model=PreguntaOut)
def create_pregunta(data: PreguntaCreate, db: Session = Depends(get_db)):
    return crud.create_pregunta(db, data)


@router.get("/", response_model=list[PreguntaOut])
def list_preguntas(db: Session = Depends(get_db)):
    return crud.get_preguntas(db)


@router.get("/{pregunta_id}", response_model=PreguntaOut)
def get_pregunta(pregunta_id, db: Session = Depends(get_db)):
    obj = crud.get_pregunta(db, pregunta_id)
    if not obj:
        raise HTTPException(404, "Pregunta no encontrada")
    return obj


@router.put("/{pregunta_id}", response_model=PreguntaOut)
def update_pregunta(
    pregunta_id,
    data: PreguntaUpdate,
    db: Session = Depends(get_db),
):
    obj = crud.update_pregunta(db, pregunta_id, data)
    if not obj:
        raise HTTPException(404, "Pregunta no encontrada")
    return obj


@router.delete("/{pregunta_id}")
def delete_pregunta(pregunta_id, db: Session = Depends(get_db)):
    obj = crud.delete_pregunta(db, pregunta_id)
    if not obj:
        raise HTTPException(404, "Pregunta no encontrada")
    return {"ok": True}