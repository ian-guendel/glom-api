import uuid
from sqlalchemy import Column, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base


class Pregunta(Base):
    __tablename__ = "preguntas"

    id_pregunta = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_reto = Column(
        UUID(as_uuid=True),
        ForeignKey("retos.id_reto", ondelete="CASCADE"),
        nullable=False
    )
    enunciado = Column(Text, nullable=False)