from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

class ExpensesForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    who = StringField('Komu', validators=[DataRequired()])
    description = TextAreaField('Opis', validators=[DataRequired()])
    number = StringField('Ile', validators=[DataRequired()])
    done = BooleanField('Opłacone?', validators=[DataRequired()])