from sqlalchemy.orm import Session
from app.models.respuesta import Respuesta
from app.schemas.respuesta import RespuestaCreate, RespuestaUpdate


def create_respuesta(db: Session, data: RespuestaCreate) -> Respuesta:
    obj = Respuesta(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def get_respuesta(db: Session, respuesta_id):
    return db.query(Respuesta).filter_by(id_respuesta=respuesta_id).first()


def get_respuestas(db: Session):
    return db.query(Respuesta).all()


def update_respuesta(db: Session, respuesta_id, data: RespuestaUpdate):
    obj = get_respuesta(db, respuesta_id)
    if not obj:
        return None
    for field, value in data.dict(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


def delete_respuesta(db: Session, respuesta_id):
    obj = get_respuesta(db, respuesta_id)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj