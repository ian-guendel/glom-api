from sqlalchemy.orm import Session

from app.models.intento import Intento
from app.schemas.intento import IntentoCreate
from app.services.progreso import recalcular_progreso


def create_intento(db: Session, data: IntentoCreate) -> Intento:
    intento = Intento(**data.dict())
    db.add(intento)
    db.commit()
    db.refresh(intento)

    # 🔥 AQUÍ ocurre la magia cognitiva
    recalcular_progreso(
        db=db,
        id_estudiante=intento.id_estudiante,
        id_tema=intento.id_tema,
    )

    return intento


def get_intento(db: Session, intento_id):
    return db.query(Intento).filter_by(id_intento=intento_id).first()


def get_intentos(db: Session):
    return db.query(Intento).all()