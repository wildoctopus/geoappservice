from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from wtforms import SubmitField

class UploadForm(FlaskForm):
    file = FileField('File', [FileRequired()])
    submit = SubmitField('Submit')