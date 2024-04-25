from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FileField
from wtforms.validators import InputRequired, NumberRange
from flask_wtf.file import FileRequired, FileAllowed


class AddProductForm(FlaskForm):
    name = StringField('Product Name', validators=[InputRequired()])
    price = IntegerField('Price', validators=[InputRequired(), NumberRange(min=0)])
    quantity = IntegerField('Quantity', validators=[InputRequired(), NumberRange(min=1)])
    image = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'])])
