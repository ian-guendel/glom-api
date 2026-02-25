from sqlalchemy.orm import Session
from app.models.estudiante import Estudiante
from app.schemas.estudiante import EstudianteCreate, EstudianteUpdate


def create_estudiante(db: Session, data: EstudianteCreate) -> Estudiante:
    obj = Estudiante(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def get_estudiante(db: Session, estudiante_id):
    return db.query(Estudiante).filter_by(id_estudiante=estudiante_id).first()


def get_estudiantes(db: Session):
    return db.query(Estudiante).all()


def update_estudiante(db: Session, estudiante_id, data: EstudianteUpdate):
    obj = get_estudiante(db, estudiante_id)
    if not obj:
        return None
    for field, value in data.dict(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


def delete_estudiante(db: Session, estudiante_id):
    obj = get_estudiante(db, estudiante_id)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj