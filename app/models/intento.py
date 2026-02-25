import uuid
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.core.database import Base


resultado_enum = Enum(
    "correcto",
    "incorrecto",
    "abandono",
    name="resultado_enum"
)


class Intento(Base):
    __tablename__ = "intentos"

    id_intento = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    id_estudiante = Column(
        UUID(as_uuid=True),
        ForeignKey("estudiantes.id_estudiante"),
        nullable=False
    )

    id_reto = Column(
        UUID(as_uuid=True),
        ForeignKey("retos.id_reto"),
        nullable=False
    )

    id_tema = Column(
        UUID(as_uuid=True),
        ForeignKey("temas.id_tema"),
        nullable=False
    )

    nivel = Column(Integer, nullable=False)
    numero_intento = Column(Integer, nullable=False)

    resultado = Column(resultado_enum, nullable=False)

    tiempo_segundos = Column(Integer)
    timestamp = Column(DateTime, server_default=func.now())