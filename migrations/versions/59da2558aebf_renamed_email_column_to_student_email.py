"""Renamed email column to student_email

Revision ID: 59da2558aebf
Revises: 
Create Date: 2025-04-27 14:41:09.710365

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '59da2558aebf'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('students', 'email', new_column_name='student_email')

def downgrade() -> None:
    op.alter_column('students', 'student_email', new_column_name='email')

