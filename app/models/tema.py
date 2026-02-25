import uuid
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base

class Tema(Base):
    __tablename__ = "temas"

    id_tema = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String, nullable=False)
    materia = Column(String, nullable=False)
    grado = Column(Integer, nullable=False)
    orden_logico = Column(Integer)
    activo = Column(Boolean, default=True)