"""Make more columns nullable

Revision ID: bffd6f627419
Revises: 4b29622204a8
Create Date: 2025-04-01 10:46:26.877056

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bffd6f627419'
down_revision: Union[str, None] = '4b29622204a8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('crypto_currency', 'hashing_algorithm',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('crypto_currency', 'hashing_algorithm',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
