"""Crear tabla pedido_status_history

Revision ID: a6678775133c
Revises: 2741628cc061
Create Date: 2025-05-29 14:01:56.340815

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a6678775133c'
down_revision: Union[str, None] = '2741628cc061'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'pedido_status_history',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('pedido_id', sa.Integer(), sa.ForeignKey(
            'pedidos.id'), nullable=False),
        sa.Column('estatus_anterior', sa.String(length=50), nullable=False),
        sa.Column('estatus_nuevo', sa.String(length=50), nullable=False),
        sa.Column('creado_en', sa.DateTime(timezone=True),
                  server_default=sa.func.now(), nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
