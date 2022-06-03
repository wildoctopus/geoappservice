"""Form object declaration."""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):
    """Add Airport form."""

    name = StringField('Name', [DataRequired()])
    longitude = FloatField('Long', [DataRequired()])
    latitude = FloatField('Lat', [DataRequired()])
    
    submit = SubmitField('Submit')