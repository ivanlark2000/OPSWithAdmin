from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, StringField, TextAreaField, SubmitField
from wtforms.validators import ValidationError, Email, EqualTo, DataRequired, Length


class Authorization(FlaskForm):
    user = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Подтвердить')