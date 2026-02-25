from sqlalchemy.orm import Session
from app.models.pregunta import Pregunta
from app.schemas.pregunta import PreguntaCreate, PreguntaUpdate


def create_pregunta(db: Session, data: PreguntaCreate) -> Pregunta:
    obj = Pregunta(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def get_pregunta(db: Session, pregunta_id):
    return db.query(Pregunta).filter_by(id_pregunta=pregunta_id).first()


def get_preguntas(db: Session):
    return db.query(Pregunta).all()


def update_pregunta(db: Session, pregunta_id, data: PreguntaUpdate):
    obj = get_pregunta(db, pregunta_id)
    if not obj:
        return None
    for field, value in data.dict(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


def delete_pregunta(db: Session, pregunta_id):
    obj = get_pregunta(db, pregunta_id)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj