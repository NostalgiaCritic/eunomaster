from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    name = StringField('성함', validators=[DataRequired("성함은 필수입력 항목입니다.")])
    number = StringField('전화번호', validators=[DataRequired("전화번호는 필수입력 항목입니다.")])
