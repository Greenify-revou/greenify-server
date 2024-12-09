"""fix carts table

Revision ID: c5ba8d9a2787
Revises: f628ac4d9d0d
Create Date: 2024-12-09 17:15:34.694604

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5ba8d9a2787'
down_revision = 'f628ac4d9d0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('carts', schema=None) as batch_op:
        batch_op.drop_column('price')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('carts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price', sa.NUMERIC(precision=16, scale=2), autoincrement=False, nullable=False))

    # ### end Alembic commands ###