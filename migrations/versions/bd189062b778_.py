"""empty message

Revision ID: bd189062b778
Revises: 340cef248eee
Create Date: 2022-06-05 19:37:06.475774

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd189062b778'
down_revision = '340cef248eee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('flat', sa.Column('street', sa.String(length=64), nullable=False))
    op.add_column('flat', sa.Column('house', sa.Integer(), nullable=False))
    op.drop_index('ix_flat_address', table_name='flat')
    op.create_index(op.f('ix_flat_house'), 'flat', ['house'], unique=False)
    op.create_index(op.f('ix_flat_street'), 'flat', ['street'], unique=False)
    op.drop_column('flat', 'address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('flat', sa.Column('address', sa.VARCHAR(length=64), nullable=False))
    op.drop_index(op.f('ix_flat_street'), table_name='flat')
    op.drop_index(op.f('ix_flat_house'), table_name='flat')
    op.create_index('ix_flat_address', 'flat', ['address'], unique=False)
    op.drop_column('flat', 'house')
    op.drop_column('flat', 'street')
    # ### end Alembic commands ###
