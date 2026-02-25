from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.tema import TemaCreate, TemaUpdate, TemaOut
from app.crud import tema as crud

router = APIRouter(prefix="/temas", tags=["Temas"])


@router.post("/", response_model=TemaOut)
def create_tema(data: TemaCreate, db: Session = Depends(get_db)):
    return crud.create_tema(db, data)


@router.get("/", response_model=list[TemaOut])
def list_temas(db: Session = Depends(get_db)):
    return crud.get_temas(db)


@router.get("/{tema_id}", response_model=TemaOut)
def get_tema(tema_id, db: Session = Depends(get_db)):
    obj = crud.get_tema(db, tema_id)
    if not obj:
        raise HTTPException(404, "Tema no encontrado")
    return obj


@router.put("/{tema_id}", response_model=TemaOut)
def update_tema(tema_id, data: TemaUpdate, db: Session = Depends(get_db)):
    obj = crud.update_tema(db, tema_id, data)
    if not obj:
        raise HTTPException(404, "Tema no encontrado")
    return obj


@router.delete("/{tema_id}")
def delete_tema(tema_id, db: Session = Depends(get_db)):
    obj = crud.delete_tema(db, tema_id)
    if not obj:
        raise HTTPException(404, "Tema no encontrado")
    return {"ok": True}