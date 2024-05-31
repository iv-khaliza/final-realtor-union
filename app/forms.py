from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
import sqlalchemy as sa
from app import app, db
from app.models import Company, Flat

class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sing In')

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password1 = PasswordField('Repeat password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, name):
        name = db.session.scalar(sa.select(Company).where(
            Company.username == name.data))
        if name is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        name = db.session.scalar(sa.select(Company).where(
            Company.email == email.data))
        if name is not None:
            raise ValidationError('Please use a different email address.')

class EditProfileForm(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])
    phone = StringField('Phone me', validators=[DataRequired()])
    body = TextAreaField('About me', validators=[Length(min=0, max=512)])
    submit = SubmitField('Submit')

class AddOffer(FlaskForm):
    img = StringField('Img', validators=[DataRequired()])
    flat_type = StringField('Flat type', validators=[DataRequired()])
    offer_type = SelectField('Type of offer', choices=[('sa', 'Sale'), ('re', 'Rent'), ('ot', 'Other')])
    price = StringField('Price', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    square = StringField('Square', validators=[DataRequired()])
    nor = StringField('Number of rooms', validators=[DataRequired()])
    body = TextAreaField('About me', validators=[Length(min=0, max=512)])
    submit = SubmitField('Submit')

class SimpleForm(FlaskForm):
    type_f = SelectField('Type of flat', choices=[('py', 'Python')])
    submit = SubmitField('Submit')
