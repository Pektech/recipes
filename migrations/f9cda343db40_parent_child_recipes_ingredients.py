"""parent child recipes ingredients

Revision ID: f9cda343db40
Revises: e1c6571af7ad
Create Date: 2018-06-10 12:34:57.520481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9cda343db40'
down_revision = 'e1c6571af7ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipe_uses',
    sa.Column('recipes_id', sa.Integer(), nullable=False),
    sa.Column('ingredients_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ingredients_id'], ['ingredients.id'], ),
    sa.ForeignKeyConstraint(['recipes_id'], ['recipes.id'], ),
    sa.PrimaryKeyConstraint('recipes_id', 'ingredients_id')
    )
    op.drop_column('recipes', 'ingred')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipes', sa.Column('ingred', sa.INTEGER(), nullable=True))
    op.drop_table('recipe_uses')
    # ### end Alembic commands ###
