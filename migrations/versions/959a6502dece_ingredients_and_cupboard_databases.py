"""ingredients and cupboard databases

Revision ID: 959a6502dece
Revises: 22906c39bdef
Create Date: 2018-06-09 12:47:03.574157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '959a6502dece'
down_revision = '22906c39bdef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ingredients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ing_name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ingredients_ing_name'), 'ingredients', ['ing_name'], unique=True)
    op.create_table('cupboard',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('ingred', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ingred'], ['ingredients.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cupboard')
    op.drop_index(op.f('ix_ingredients_ing_name'), table_name='ingredients')
    op.drop_table('ingredients')
    # ### end Alembic commands ###
