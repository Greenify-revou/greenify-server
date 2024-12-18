"""add new transaction_history tables

Revision ID: 03f99501e1e0
Revises: 3663af35fe6e
Create Date: 2024-12-11 21:35:34.902894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03f99501e1e0'
down_revision = '3663af35fe6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transactions_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('invoice_number', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('seller_id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Numeric(precision=16, scale=2), nullable=True),
    sa.Column('eco_point', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('voucher_id', sa.Integer(), nullable=True),
    sa.Column('discount', sa.Float(), nullable=True),
    sa.Column('status', sa.Enum('CANCELLED', 'COMPLETED', name='transactionstatus'), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['seller_id'], ['seller_profile.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['voucher_id'], ['voucher.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('order_items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('voucher_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'voucher', ['voucher_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order_items', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('voucher_id')

    op.drop_table('transactions_history')
    # ### end Alembic commands ###