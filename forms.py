from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SentimentForm(FlaskForm):
    
    user_string = StringField(label='Enter the string', validators=[DataRequired()])
    submit = SubmitField(label='Check for Sentiment')