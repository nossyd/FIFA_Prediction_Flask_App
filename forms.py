from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import NumberRange, DataRequired

error_message = "Please enter a number between 0 and 100"

class OvrPredictForm(FlaskForm):
    # General Attributes
    pace = IntegerField('Pace', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])
    shoot = IntegerField('Shooting', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])
    passing = IntegerField('Passing', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])
    dribble = IntegerField('Dribble', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])
    defend = IntegerField('Defend', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])
    physic = IntegerField('Physic', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])

    # Attacking Attributes
    crossing = IntegerField('Crossing', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])
    finishing = IntegerField('Finishing', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])
    heading = IntegerField('Heading', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])
    short_pass = IntegerField('Short Passing', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])
    volleys = IntegerField('Volleys', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])

    # Skills Attributes
    skill_dribbling = IntegerField('Skill Dribbling', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])
    fk_accuracy = IntegerField('Free Kicks', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])
    long_pass = IntegerField('Long Passes', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])
    ball_control = IntegerField('Ball Control', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])

    # Movement Attributes
    aggression = IntegerField('Aggression', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])
    interceptions = IntegerField('Interceptions', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])
    positioning = IntegerField('Positioning', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])
    vision = IntegerField('Vision', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])
    penalties = IntegerField('Penalties', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])
    composure = IntegerField('Composure', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])

    # Defending Attributes
    marking = IntegerField('Marking', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])
    stand_tackle = IntegerField('Standing Tackle', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])
    slide_tackle = IntegerField('Sliding Tackle', validators=[NumberRange(min=0, max=99, message=error_message), DataRequired(message=error_message)])

    submit = SubmitField('Submit')