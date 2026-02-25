import uuid
from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base


class Reto(Base):
    __tablename__ = "retos"

    id_reto = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_tema = Column(UUID(as_uuid=True), ForeignKey("temas.id_tema"), nullable=False)
    nivel = Column(Integer, nullable=False)
    activo = Column(Boolean, default=True)