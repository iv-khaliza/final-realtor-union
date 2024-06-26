"""flat_s table

Revision ID: bc68cce19696
Revises: d5ff581f1a5d
Create Date: 2024-05-30 19:06:20.065497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc68cce19696'
down_revision = 'd5ff581f1a5d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flat_s',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('f_type', sa.String(length=32), nullable=False),
    sa.Column('price', sa.String(length=16), nullable=False),
    sa.Column('address', sa.String(length=64), nullable=False),
    sa.Column('img', sa.String(length=256), nullable=True),
    sa.Column('square', sa.String(length=64), nullable=True),
    sa.Column('num_of_rooms', sa.Integer(), nullable=True),
    sa.Column('body', sa.String(length=512), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('flat_s', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_flat_s_company_id'), ['company_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_flat_s_price'), ['price'], unique=False)
        batch_op.create_index(batch_op.f('ix_flat_s_square'), ['square'], unique=False)
        batch_op.create_index(batch_op.f('ix_flat_s_timestamp'), ['timestamp'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('flat_s', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_flat_s_timestamp'))
        batch_op.drop_index(batch_op.f('ix_flat_s_square'))
        batch_op.drop_index(batch_op.f('ix_flat_s_price'))
        batch_op.drop_index(batch_op.f('ix_flat_s_company_id'))

    op.drop_table('flat_s')
    # ### end Alembic commands ###
