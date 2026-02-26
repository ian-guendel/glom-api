# 🧠 GloM -- Infraestructura Cognitiva Educativa

GloM es una **infraestructura backend** diseñada para transformar
interacciones educativas (retos, preguntas, respuestas e intentos) en
**datos estructurados de progreso cognitivo medible**.

> ❌ GloM NO es un LMS tradicional\
> ❌ GloM NO es un chatbot educativo\
> ✅ GloM es infraestructura cognitiva basada en datos

------------------------------------------------------------------------

## 🧱 Stack Tecnológico

-   Backend: FastAPI\
-   Base de datos: PostgreSQL\
-   ORM: SQLAlchemy\
-   Migraciones: Alembic\
-   Contenedores: Podman + Podman Compose\
-   Configuración: Variables de entorno (.env)

------------------------------------------------------------------------

## 📁 Estructura del Proyecto

    .
    ├── app/
    │   ├── api/v1/
    │   ├── core/
    │   ├── crud/
    │   ├── models/
    │   ├── schemas/
    │   ├── services/
    │   └── main.py
    ├── alembic/
    │   ├── versions/
    │   └── env.py
    ├── podman-compose.yml
    ├── .env
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## ⚙️ Requisitos Previos

-   Python 3.10+
-   Podman
-   Podman Compose

Verificar instalación:

    podman --version
    podman-compose --version
    python --version

------------------------------------------------------------------------

## 🔐 Variables de Entorno

Crear un archivo `.env` en el root del proyecto:

    POSTGRES_USER=glom_user
    POSTGRES_PASSWORD=glom_password
    POSTGRES_DB=glom_db
    POSTGRES_HOST=localhost
    POSTGRES_PORT=5432

    DATABASE_URL=postgresql+psycopg2://glom_user:glom_password@localhost:5432/glom_db

------------------------------------------------------------------------

## 🐘 Levantar Servicios con Podman

### 1. Iniciar Podman (macOS / Windows)

    podman machine init
    podman machine start

Verificar:

    podman info

------------------------------------------------------------------------

### 2. Levantar PostgreSQL y pgAdmin

    podman-compose up -d

Servicios: - PostgreSQL: localhost:5432 - pgAdmin: http://localhost:5050

------------------------------------------------------------------------

## 🧪 Backend

### 3. Crear entorno virtual

    python -m venv venv
    source venv/bin/activate

### 4. Instalar dependencias

    pip install -r requirements.txt

------------------------------------------------------------------------

## 📦 Migraciones

    alembic upgrade head

------------------------------------------------------------------------

## 🚀 Ejecutar la Aplicación

    uvicorn app.main:app --reload

-   API: http://localhost:8000
-   Docs: http://localhost:8000/docs

------------------------------------------------------------------------

## 📡 API Reference -- Endpoints (v1)

**Base URL:**

    http://localhost:8000/api/v1

### 👤 Estudiantes

-   POST `/estudiantes/`
-   GET `/estudiantes/`
-   GET `/estudiantes/{estudiante_id}`
-   PUT `/estudiantes/{estudiante_id}`
-   DELETE `/estudiantes/{estudiante_id}`

### 📚 Temas

-   POST `/temas/`
-   GET `/temas/`
-   GET `/temas/{tema_id}`
-   PUT `/temas/{tema_id}`
-   DELETE `/temas/{tema_id}`

### 🧠 Retos

-   POST `/retos/`
-   GET `/retos/`
-   GET `/retos/{reto_id}`
-   PUT `/retos/{reto_id}`
-   DELETE `/retos/{reto_id}`

### ❓ Preguntas

-   POST `/preguntas/`
-   GET `/preguntas/`
-   GET `/preguntas/{pregunta_id}`
-   PUT `/preguntas/{pregunta_id}`
-   DELETE `/preguntas/{pregunta_id}`

### 🅰️ Respuestas

-   POST `/respuestas/`
-   GET `/respuestas/`
-   GET `/respuestas/{respuesta_id}`
-   PUT `/respuestas/{respuesta_id}`
-   DELETE `/respuestas/{respuesta_id}`

### 🧪 Intentos

-   POST `/intentos/`
-   GET `/intentos/`
-   GET `/intentos/{intento_id}`

> Nota: Al crear un intento, el sistema recalcula automáticamente el
> progreso cognitivo.

------------------------------------------------------------------------

## 🧠 Flujo Cognitivo

Cada intento recalcula automáticamente el progreso cognitivo del
estudiante por tema.

Lógica principal en:

    app/services/progreso.py

------------------------------------------------------------------------