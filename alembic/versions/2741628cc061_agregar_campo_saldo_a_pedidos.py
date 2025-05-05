"""Agregar campo saldo a pedidos

Revision ID: 2741628cc061
Revises: 6edb7877db41
Create Date: 2025-05-04 18:25:48.332279

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2741628cc061'
down_revision: Union[str, None] = '6edb7877db41'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('pedidos', sa.Column('saldo', sa.Float(),
                  nullable=False, server_default='0.0'))


def downgrade() -> None:
    op.drop_column('pedidos', 'saldo')
