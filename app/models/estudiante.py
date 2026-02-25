import uuid
from sqlalchemy import Column, Integer, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.core.database import Base


class Estudiante(Base):
    __tablename__ = "estudiantes"

    id_estudiante = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    grado = Column(Integer, nullable=False)
    activo = Column(Boolean, default=True)
    fecha_alta = Column(DateTime, server_default=func.now())