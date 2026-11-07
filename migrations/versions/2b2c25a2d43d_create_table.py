"""create_table

Revision ID: 2b2c25a2d43d
Revises: 
Create Date: 2026-11-07 22:52:58.039816

"""
from collections.abc import Sequence

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '2b2c25a2d43d'
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.execute("""
           CREATE TABLE users (
               user_id BIGINT PRIMARY KEY,
               city VARCHAR(100),
               notify_time TIME DEFAULT '08:00'
           )
       """)


def downgrade() -> None:
    op.execute("DROP TABLE users")