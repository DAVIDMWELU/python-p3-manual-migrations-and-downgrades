"""Create students table

Revision ID: ac8084fbc216
Revises: 59da2558aebf
Create Date: 2025-04-27 14:44:34.576626

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ac8084fbc216'
down_revision: Union[str, None] = '59da2558aebf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'students',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
