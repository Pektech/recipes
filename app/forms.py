from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import widgets, SelectMultipleField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User, Ingredients, Cupboard


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')



class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')



class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=True)
    option_widget = widgets.CheckboxInput()



class AddDeleteForm(FlaskForm):
    results = Ingredients.query.all()
    ing_list = [(x.id, x.ing_name) for x in results]
    example = MultiCheckboxField('Label', choices=ing_list, coerce=int)
    submit1 = SubmitField('Add')
    submit2 = SubmitField('Delete')


class AddRecipe(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    info = TextAreaField('Info', validators=[DataRequired()])
    rec_type = SelectField('type', choices=[('heat', 'Heat'), ('health', 'Health')])
    results = Ingredients.query.all()
    ing_list = [(x.id, x.ing_name) for x in results]
    recipe_needs = MultiCheckboxField('Label', choices=ing_list, coerce=int)
    submit = SubmitField("Add")