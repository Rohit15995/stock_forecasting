from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PredictionForm(FlaskForm):
    stock = StringField('Stock', validators=[DataRequired()])
    forecast_date = StringField('Forecast Date', validators=[DataRequired()])
    submit = SubmitField('Predict')