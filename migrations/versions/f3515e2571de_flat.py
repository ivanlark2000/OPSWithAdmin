"""Flat

Revision ID: f3515e2571de
Revises: 6125ed84aad7
Create Date: 2022-05-20 09:16:31.780378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3515e2571de'
down_revision = '6125ed84aad7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flat',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('address', sa.String(length=64), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('district', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_flat_address'), 'flat', ['address'], unique=False)
    op.create_index(op.f('ix_flat_district'), 'flat', ['district'], unique=False)
    op.create_index(op.f('ix_flat_price'), 'flat', ['price'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_flat_price'), table_name='flat')
    op.drop_index(op.f('ix_flat_district'), table_name='flat')
    op.drop_index(op.f('ix_flat_address'), table_name='flat')
    op.drop_table('flat')
    # ### end Alembic commands ###