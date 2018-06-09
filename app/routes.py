from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from app.forms import LoginForm
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/login', methods=["GET", "POST"])
def login():

    form = LoginForm()
    if form.validate_on_submit():

        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register')
def register():
    return('register')

