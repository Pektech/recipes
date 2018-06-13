from app.models import Ingredients, User, Recipes
from app  import db




ing_list = ['Apple', 'Tabantha Wheat', 'Wildberry', 'Monster Extract',
              'Acorn', 'Swift Carrot', 'Fresh Milk', 'Bird Egg', 'Hylian Rice',
              'Raw Meat',  'Raw Gourmet Meat', 'Raw Whole Bird',
              'Raw Bird Drumstick', 'Spicy Pepper',
              'Hyrule Shroom', 'Hyrule Herb', 'Hyrule Bass',
              'Rock Salt', 'Endura Shroom',
              'Courser Bee Honey', 'Palm Fruit', 'Hearty Radish',
              'Raw Prime Meat', 'Hearty Blueshell Snail', 'Hearty Truffle',
              'Endura Carrot', 'Goat Butter', "Cane Sugar"]

def bulkIngredAdd(ing_list):
    for item in ing_list:
        db.session.add(Ingredients(
            ing_name=item
        ))
    db.session.commit()



def list_ingredients2(recipe):
    for item in recipe:
        print(item.ing_name)

def list_cup_ing(recipe):
    for item in recipe:
        print(item.ingred)

def find_recipes():
    user = User.query.filter(User.username=='tom').first()





# newtest = db.session.query(Recipes.id, func.count(Ingredients.id)).join(Recipes.contains).group_by(Recipes.id).having(func.count(Ingredients.id)==2)
# this will find recipes that have n ingredinets, return s tulpe (recipe id, n)


