"""trying to add recipes treating recipes like a cupboard

Revision ID: e143261faf0d
Revises: e1c6571af7ad
Create Date: 2018-06-10 11:28:51.307333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e143261faf0d'
down_revision = 'e1c6571af7ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipes_ingreds')
    op.add_column('recipes', sa.Column('ingred', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'recipes', 'ingredients', ['ingred'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'recipes', type_='foreignkey')
    op.drop_column('recipes', 'ingred')
    op.create_table('recipes_ingreds',
    sa.Column('recipe_id', sa.INTEGER(), nullable=True),
    sa.Column('ingred_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['ingred_id'], ['ingredients.id'], ),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.id'], )
    )
    # ### end Alembic commands ###
