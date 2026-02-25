from sqlalchemy.orm import Session
from app.models.reto import Reto
from app.schemas.reto import RetoCreate, RetoUpdate


def create_reto(db: Session, data: RetoCreate) -> Reto:
    obj = Reto(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def get_reto(db: Session, reto_id):
    return db.query(Reto).filter_by(id_reto=reto_id).first()


def get_retos(db: Session):
    return db.query(Reto).all()


def update_reto(db: Session, reto_id, data: RetoUpdate):
    obj = get_reto(db, reto_id)
    if not obj:
        return None
    for field, value in data.dict(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


def delete_reto(db: Session, reto_id):
    obj = get_reto(db, reto_id)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj