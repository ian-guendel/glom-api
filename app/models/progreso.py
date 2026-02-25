from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.core.database import Base


class ProgresoTemaEstudiante(Base):
    __tablename__ = "progreso_tema_estudiante"

    id_estudiante = Column(UUID(as_uuid=True), primary_key=True)
    id_tema = Column(UUID(as_uuid=True), primary_key=True)

    nivel_actual = Column(Integer)
    intentos_totales = Column(Integer)
    aciertos_totales = Column(Integer)
    errores_totales = Column(Integer)

    tasa_error = Column(Float)
    porcentaje_dominio = Column(Float)

    ultima_actualizacion = Column(DateTime, server_default=func.now())