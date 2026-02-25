from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.intento import IntentoCreate, IntentoOut
from app.crud import intento as crud

router = APIRouter(prefix="/intentos", tags=["Intentos"])


@router.post("/", response_model=IntentoOut)
def create_intento(data: IntentoCreate, db: Session = Depends(get_db)):
    return crud.create_intento(db, data)


@router.get("/", response_model=list[IntentoOut])
def list_intentos(db: Session = Depends(get_db)):
    return crud.get_intentos(db)


@router.get("/{intento_id}", response_model=IntentoOut)
def get_intento(intento_id, db: Session = Depends(get_db)):
    obj = crud.get_intento(db, intento_id)
    if not obj:
        raise HTTPException(404, "Intento no encontrado")
    return obj