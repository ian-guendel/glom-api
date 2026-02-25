"""
Initial GloM schema

Revision ID: 0001_initial_glom
Revises:
Create Date: 2026-02-24
"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy.dialects.postgresql as pg

revision = "0001_initial_glom"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():

    # =========================
    # estudiantes
    # =========================
    op.create_table(
        "estudiantes",
        sa.Column("id_estudiante", pg.UUID(as_uuid=True), primary_key=True),
        sa.Column("grado", sa.Integer(), nullable=False),
        sa.Column("fecha_registro", sa.DateTime(), server_default=sa.func.now()),
        sa.Column("activo", sa.Boolean(), server_default=sa.true())
    )

    # =========================
    # temas
    # =========================
    op.create_table(
        "temas",
        sa.Column("id_tema", pg.UUID(as_uuid=True), primary_key=True),
        sa.Column("nombre", sa.String(), nullable=False),
        sa.Column("materia", sa.String(), nullable=False),
        sa.Column("grado", sa.Integer(), nullable=False),
        sa.Column("orden_logico", sa.Integer()),
        sa.Column("activo", sa.Boolean(), server_default=sa.true()),
        sa.Column("fecha_registro", sa.DateTime(), server_default=sa.func.now())
    )

    # =========================
    # retos
    # =========================
    op.create_table(
        "retos",
        sa.Column("id_reto", pg.UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "id_tema",
            pg.UUID(as_uuid=True),
            sa.ForeignKey("temas.id_tema"),
            nullable=False
        ),
        sa.Column("nivel", sa.Integer(), nullable=False),
        sa.Column("activo", sa.Boolean(), server_default=sa.true()),
        sa.Column("fecha_registro", sa.DateTime(), server_default=sa.func.now()),
    )

    # =========================
    # preguntas
    # =========================
    op.create_table(
        "preguntas",
        sa.Column("id_pregunta", pg.UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "id_reto",
            pg.UUID(as_uuid=True),
            sa.ForeignKey("retos.id_reto", ondelete="CASCADE"),
            nullable=False
        ),
        sa.Column("enunciado", sa.Text(), nullable=False)
    )

    # =========================
    # respuestas
    # =========================
    op.create_table(
        "respuestas",
        sa.Column("id_respuesta", pg.UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "id_pregunta",
            pg.UUID(as_uuid=True),
            sa.ForeignKey("preguntas.id_pregunta", ondelete="CASCADE"),
            nullable=False
        ),
        sa.Column("texto", sa.Text(), nullable=False),
        sa.Column(
            "correcta",
            sa.Boolean(),
            nullable=False,
            server_default=sa.false()
        )
    )

    # =========================
    # enum resultado
    # =========================
    resultado_enum = sa.Enum(
        "correcto",
        "incorrecto",
        "abandono",
        name="resultado_enum"
    )
    resultado_enum.create(op.get_bind())

    # =========================
    # intentos (núcleo cognitivo)
    # =========================
    op.create_table(
        "intentos",
        sa.Column("id_intento", pg.UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "id_estudiante",
            pg.UUID(as_uuid=True),
            sa.ForeignKey("estudiantes.id_estudiante"),
            nullable=False
        ),
        sa.Column(
            "id_reto",
            pg.UUID(as_uuid=True),
            sa.ForeignKey("retos.id_reto"),
            nullable=False
        ),
        sa.Column(
            "id_tema",
            pg.UUID(as_uuid=True),
            sa.ForeignKey("temas.id_tema"),
            nullable=False
        ),
        sa.Column("nivel", sa.Integer(), nullable=False),
        sa.Column("numero_intento", sa.Integer(), nullable=False),
        sa.Column("resultado", resultado_enum, nullable=False),
        sa.Column("tiempo_segundos", sa.Integer()),
        sa.Column("timestamp", sa.DateTime(), server_default=sa.func.now())
    )

    # =========================
    # progreso derivado por tema
    # =========================
    op.create_table(
        "progreso_tema_estudiante",
        sa.Column("id_estudiante", pg.UUID(as_uuid=True)),
        sa.Column("id_tema", pg.UUID(as_uuid=True)),
        sa.Column("nivel_actual", sa.Integer()),
        sa.Column("intentos_totales", sa.Integer()),
        sa.Column("aciertos_totales", sa.Integer()),
        sa.Column("errores_totales", sa.Integer()),
        sa.Column("tasa_error", sa.Float()),
        sa.Column("porcentaje_dominio", sa.Float()),
        sa.Column("ultima_actualizacion", sa.DateTime(), server_default=sa.func.now()),
        sa.PrimaryKeyConstraint("id_estudiante", "id_tema")
    )

    # =========================
    # diagnosticos
    # =========================
    op.create_table(
        "diagnosticos",
        sa.Column("id_diagnostico", pg.UUID(as_uuid=True), primary_key=True),
        sa.Column("id_estudiante", pg.UUID(as_uuid=True)),
        sa.Column("id_tema", pg.UUID(as_uuid=True)),
        sa.Column("nivel_detectado", sa.Integer()),
        sa.Column("fecha", sa.DateTime(), server_default=sa.func.now())
    )

    # =========================
    # índices críticos
    # =========================
    op.create_index("idx_intentos_estudiante", "intentos", ["id_estudiante"])
    op.create_index("idx_intentos_tema", "intentos", ["id_tema"])
    op.create_index("idx_intentos_timestamp", "intentos", ["timestamp"])
    op.create_index("idx_preguntas_reto", "preguntas", ["id_reto"])
    op.create_index("idx_respuestas_pregunta", "respuestas", ["id_pregunta"])


def downgrade():

    op.drop_index("idx_respuestas_pregunta")
    op.drop_index("idx_preguntas_reto")
    op.drop_index("idx_intentos_timestamp")
    op.drop_index("idx_intentos_tema")
    op.drop_index("idx_intentos_estudiante")

    op.drop_table("diagnosticos")
    op.drop_table("progreso_tema_estudiante")
    op.drop_table("intentos")
    op.drop_table("respuestas")
    op.drop_table("preguntas")
    op.drop_table("retos")
    op.drop_table("temas")
    op.drop_table("estudiantes")

    sa.Enum(name="resultado_enum").drop(op.get_bind())