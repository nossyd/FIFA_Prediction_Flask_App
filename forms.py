from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import NumberRange, DataRequired

error_message = "Please enter a number between 0 and 100"

class OvrPredictForm(FlaskForm):
    pace = IntegerField('Pace', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])
    shoot = IntegerField('Shooting', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])
    passing = IntegerField('Passing', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])
    dribble = IntegerField('Dribble', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])
    defend = IntegerField('Defend', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])
    physic = IntegerField('Physic', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])
    submit = SubmitField('Submit')