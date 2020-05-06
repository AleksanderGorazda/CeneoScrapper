from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp

class ProductFrom(FlaskForm):
    product_code = StringField("Podaj kod produktu do pobrania opinii", 
    validators=[
        DataRequired(message='Musisz podac kod produktu'),
        Length(min = 8, max = 8, message="Kod produktu musi miec 8 znaków"),
        Regexp(regex = "^[0-9]+$", message="Kod produkutu musi moze zawierac tylko cyfry")
        ]
    )
    submit = SubmitField("Pobierz")