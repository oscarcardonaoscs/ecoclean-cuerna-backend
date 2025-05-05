"""Agregar campos monto_recibido y monto_cambio a pagos

Revision ID: 6edb7877db41
Revises: 3b929c0644ec
Create Date: 2025-05-04 15:55:21.556837

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6edb7877db41'
down_revision: Union[str, None] = '3b929c0644ec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('pagos', sa.Column('monto_recibido', sa.DECIMAL(
        10, 4), nullable=False, server_default='0'))
    op.add_column('pagos', sa.Column('monto_cambio', sa.DECIMAL(
        10, 4), nullable=False, server_default='0'))


def downgrade() -> None:
    op.drop_column('pagos', 'monto_cambio')
    op.drop_column('pagos', 'monto_recibido')
