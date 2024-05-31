"""flat_sale

Revision ID: da31a9133199
Revises: bc68cce19696
Create Date: 2024-05-30 20:37:06.091430

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da31a9133199'
down_revision = 'bc68cce19696'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('flat', schema=None) as batch_op:
        batch_op.add_column(sa.Column('order_type', sa.String(length=32), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('flat', schema=None) as batch_op:
        batch_op.drop_column('order_type')

    # ### end Alembic commands ###
