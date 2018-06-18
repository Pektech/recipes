from app.models import Ingredients, User, Recipes
from app  import db
from flask_login import current_user
import csv




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

def list_cup_ing(userquery):
    cupboardlist = []
    for item in  userquery.cupboard:
        cupboardlist.append(item.ingredients.ing_name)
    return cupboardlist


def find_recipes():
    user = User.query.filter(User.username=='tom').first()





# newtest = db.session.query(Recipes.id, func.count(Ingredients.id)).join(Recipes.contains).group_by(Recipes.id).having(func.count(Ingredients.id)==2)
# this will find recipes that have n ingredinets, return s tulpe (recipe id, n)

def addcsv(filename):
    with open(filename, newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        next(reader)
        for row in reader:
            parent = Recipes(recipe_name=row[0],
                             recipe_type=row[1],
                             recipe_info=row[5],
                             hearts=row[2],
                             sell_price=row[6],
                             duration=row[4],
                             strength=row[3]
                             )
            try:
                db.session.add(parent)
                db.session.commit()
                print("added recipe")
            except:
                db.session.rollback()
                print('error could not add recipe')
            try:
                for item in row[7::]:
                    item_query = Ingredients.query.filter(
                        Ingredients.ing_name == item).first()
                    parent.contains.append(item_query)
                    db.session.add(parent)
                    db.session.commit()
                    print(('added  recipe/ingred', item_query))
            except:
                db.session.rollback()
                print("could not add ingredinets")

