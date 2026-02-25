from fastapi import APIRouter

from .estudiantes import router as estudiantes_router
from .temas import router as temas_router
from .retos import router as retos_router
from .preguntas import router as preguntas_router
from .respuestas import router as respuestas_router
from .intentos import router as intentos_router

api_router = APIRouter()

api_router.include_router(estudiantes_router)
api_router.include_router(temas_router)
api_router.include_router(retos_router)
api_router.include_router(preguntas_router)
api_router.include_router(respuestas_router)
api_router.include_router(intentos_router)