from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.estudiante import (
    EstudianteCreate,
    EstudianteUpdate,
    EstudianteOut,
)
from app.crud import estudiante as crud

router = APIRouter(prefix="/estudiantes", tags=["Estudiantes"])


@router.post("/", response_model=EstudianteOut)
def create_estudiante(
    data: EstudianteCreate,
    db: Session = Depends(get_db),
):
    return crud.create_estudiante(db, data)


@router.get("/", response_model=list[EstudianteOut])
def list_estudiantes(db: Session = Depends(get_db)):
    return crud.get_estudiantes(db)


@router.get("/{estudiante_id}", response_model=EstudianteOut)
def get_estudiante(estudiante_id, db: Session = Depends(get_db)):
    obj = crud.get_estudiante(db, estudiante_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return obj


@router.put("/{estudiante_id}", response_model=EstudianteOut)
def update_estudiante(
    estudiante_id,
    data: EstudianteUpdate,
    db: Session = Depends(get_db),
):
    obj = crud.update_estudiante(db, estudiante_id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return obj


@router.delete("/{estudiante_id}")
def delete_estudiante(estudiante_id, db: Session = Depends(get_db)):
    obj = crud.delete_estudiante(db, estudiante_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return {"ok": True}