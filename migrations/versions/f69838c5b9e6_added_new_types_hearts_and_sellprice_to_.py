"""added new types, hearts and sellprice to recipes

Revision ID: f69838c5b9e6
Revises: da48be256465
Create Date: 2018-06-11 11:23:18.045865

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f69838c5b9e6'
down_revision = 'da48be256465'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipes', sa.Column('hearts', sa.Integer(), nullable=True))
    op.add_column('recipes', sa.Column('sell_price', sa.Integer(), nullable=True))
    op.drop_column('recipes', 'ingred')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipes', sa.Column('ingred', sa.INTEGER(), nullable=True))
    op.drop_column('recipes', 'sell_price')
    op.drop_column('recipes', 'hearts')
    # ### end Alembic commands ###
