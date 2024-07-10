from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField
from wtforms.validators import DataRequired, Length

class Friend(FlaskForm):
    name = StringField('name', validators = [DataRequired(), Length(min = 1, max = 100)])
