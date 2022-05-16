"""Form object declaration."""
from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField
from wtforms.validators import DataRequired


class AddLocationForm(FlaskForm):
    """Enter Location"""

    longitude = FloatField('Long', [DataRequired()])
    latitude = FloatField('Lat', [DataRequired()])
    
    submit = SubmitField('Submit')