from sqlalchemy.orm import Session
from app.models.tema import Tema
from app.schemas.tema import TemaCreate, TemaUpdate


def create_tema(db: Session, data: TemaCreate) -> Tema:
    obj = Tema(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def get_tema(db: Session, tema_id):
    return db.query(Tema).filter_by(id_tema=tema_id).first()


def get_temas(db: Session):
    return db.query(Tema).all()


def update_tema(db: Session, tema_id, data: TemaUpdate):
    obj = get_tema(db, tema_id)
    if not obj:
        return None
    for field, value in data.dict(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


def delete_tema(db: Session, tema_id):
    obj = get_tema(db, tema_id)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj