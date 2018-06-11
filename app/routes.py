from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from app.forms import LoginForm, RegistrationForm, AddDeleteForm, AddRecipe
from app import app, db
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Ingredients, Cupboard, Recipes
from sqlalchemy import and_


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('ingredients', username=current_user))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('ingredients')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



@app.route('/ingredients/<username>', methods=['POST', 'GET'])
@login_required
def ingredients(username):
    user = User.query.filter_by(username=username).first()
    form = AddDeleteForm()
    if form.validate_on_submit():
        if form.submit1.data:
            for item in form.example.data:
                result = db.session.query(Cupboard).filter(
                    Cupboard.ingred == item).first()
                if result is None:
                    try:
                        cup = Cupboard(user_id=user.id, ingred=item)
                        db.session.add(cup)
                        db.session.commit()

                    except:
                        db.session.rollback()

                else:
                    try:
                        pass
                        # db.session.query(Cupboard).filter(
                        #     Cupboard.ingred == item).update(
                        #     {'quantity': Cupboard.quantity + 1})
                        # db.session.commit()
                    except:
                        db.session.rollback()
        elif form.submit2:
            for item in form.example.data:
                result = db.session.query(Cupboard).filter(
                    Cupboard.ingred == item).first()
                if result is not None:
                    try:
                        cup = Cupboard.query.filter_by(user_id=user.id,
                                                       ingred=item).one()
                        db.session.delete(cup)
                        db.session.commit()

                    except:
                        db.session.rollback()

                else:
                    pass
    cupboard = Cupboard.query.filter_by(user_id=user.id)
    return render_template('ingredients.html',form=form, cupboard=cupboard)

@app.route('/addRecipes', methods=["POST", "GET"])
def addRecipes():
    form = AddRecipe()
    if form.validate_on_submit():
        parent = Recipes(recipe_name=form.name.data,
                         recipe_type=form.rec_type.data, recipe_info=form.info.data)

        try:
            db.session.add(parent)
            db.session.commit()
            flash("added recipe")

        except:
            db.session.rollback()
            flash('error could not add recipe')
        try:
            for item in form.recipe_needs.data:
                item_query =  Ingredients.query.filter(Ingredients.id==item).first()
                parent.contains.append(item_query)
                db.session.add(parent)
                db.session.commit()
                flash(('added  recipe/ingred', item_query))
        except:
            db.session.rollback()
            flash("could not add ingredinets")

    return render_template('addRecipes.html', form=form)