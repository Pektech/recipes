from app import app, db
from app.models import User, Ingredients, Cupboard, Recipes, recipe_uses


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Ingredients': Ingredients,
            'Cupboard': Cupboard, 'Recipes': Recipes, 'recipe_uses': recipe_uses}
