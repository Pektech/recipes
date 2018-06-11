from app.models import Ingredients
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

