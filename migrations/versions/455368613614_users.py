"""users

Revision ID: 455368613614
Revises: 08119bd8edfa
Create Date: 2018-09-24 18:46:44.587946

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '455368613614'
down_revision = '08119bd8edfa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###
