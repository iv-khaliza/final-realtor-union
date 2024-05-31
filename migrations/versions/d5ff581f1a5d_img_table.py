"""img_table

Revision ID: d5ff581f1a5d
Revises: fecd98aad7bd
Create Date: 2024-05-30 09:36:10.897361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5ff581f1a5d'
down_revision = 'fecd98aad7bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('flat', schema=None) as batch_op:
        batch_op.add_column(sa.Column('img', sa.String(length=256), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('flat', schema=None) as batch_op:
        batch_op.drop_column('img')

    # ### end Alembic commands ###
