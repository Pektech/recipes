from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin




recipe_uses = db.Table('recipe_uses',
                    db.Column('recipes_id', db.Integer, db.ForeignKey('recipes.id'),
                              primary_key=True),
                    db.Column('ingredients_id', db.Integer, db.ForeignKey('ingredients.id'),
                              primary_key=True))









class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    cupboard = db.relationship('Cupboard', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        return '<User {}>'.format(self.username)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Ingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ing_name = db.Column(db.String(64), index=True, unique=True)
    cupboard = db.relationship('Cupboard', backref='ingredient', lazy=True)




class Cupboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ingred = db.Column(db.Integer, db.ForeignKey('ingredients.id'))
    quantity = db.Column(db.Integer)


class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(120), index=True, unique=True)
    recipe_type = db.Column(db.String(30), index=True)
    recipe_info = db.Column(db.String(120), index=True)
    hearts = db.Column(db.Integer)
    sell_price = db.Column(db.Integer)
    contains = db.relationship('Ingredients',
                               secondary='recipe_uses',
                               lazy='subquery',
                               backref=db.backref('recipes', lazy=True))







