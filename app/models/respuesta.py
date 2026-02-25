import uuid
from sqlalchemy import Column, Text, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base


class Respuesta(Base):
    __tablename__ = "respuestas"

    id_respuesta = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_pregunta = Column(
        UUID(as_uuid=True),
        ForeignKey("preguntas.id_pregunta", ondelete="CASCADE"),
        nullable=False
    )
    texto = Column(Text, nullable=False)
    correcta = Column(Boolean, nullable=False, default=False)