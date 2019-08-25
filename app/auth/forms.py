from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from app.models import User

class LoginForm (FlaskForm):
    username = StringField('Ваше имя', validators=[DataRequired()])
    password = PasswordField('Ваш пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Отправить!')

class ReqistrationForm(FlaskForm):
    username = StringField('Ваше имя', validators=[DataRequired()])
    email = StringField('Ваша электронная почта', validators=[DataRequired(), Email()])
    password = PasswordField('Ваш пароль', validators=[DataRequired()])
    password2 = PasswordField('Повторите Ваш пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError ('Такое имя уже существует. Пожалуйста, введите новое имя!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError ('Такой почтовый адрес уже существует. Пожалуйста, введите новый адрес!')


class ResetPasswordRequestForm (FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Запрос сброса пароля')

class ResetPasswordForm (FlaskForm):
    password = PasswordField('Ваш пароль', validators=[DataRequired()])
    password2 = PasswordField('Повторите Ваш пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Произвести сброс пароля')