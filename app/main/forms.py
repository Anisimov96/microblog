from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length

from app.models import User

class EditProfileForm(FlaskForm):
    username = StringField ('Ваше имя', validators=[DataRequired()])
    about_me = TextAreaField ('Обо мне', validators=[Length(min=0, max=140)])
    submit = SubmitField('Представить')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm,self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError ('Пожалуйста введите новое имя')

class PostForm (FlaskForm):
    post = TextAreaField ('Расскажите что-нибудь:', validators=[DataRequired() ,Length(min=1, max=140)])
    submit = SubmitField('Рассказать')

class SearchForm(FlaskForm):
    q = StringField(('Поиск'), validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formatdata'] = request.args
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        super(SearchForm, self).__init__(*args, **kwargs)