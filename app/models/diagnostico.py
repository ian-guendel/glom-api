import uuid
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.core.database import Base


class Diagnostico(Base):
    __tablename__ = "diagnosticos"

    id_diagnostico = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_estudiante = Column(UUID(as_uuid=True))
    id_tema = Column(UUID(as_uuid=True))
    nivel_detectado = Column(Integer)
    fecha = Column(DateTime, server_default=func.now())