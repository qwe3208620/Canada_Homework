from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import InputRequired, Length, Email, DataRequired
from wtforms.fields.html5 import EmailField


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(min=3, max=15)])
    email = EmailField('Email', validators=[InputRequired(), Email()])
    message = TextAreaField('Message / Special instructions',
                            validators=[InputRequired()],
                            render_kw={'rows': 7})
    submit = SubmitField('SEND MESSAGE')


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('login')