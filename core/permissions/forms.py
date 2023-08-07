from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, SubmitField, SelectField
from wtforms import validators


class CreateRolesForm(FlaskForm):
    name = StringField('Name', validators=[validators.data_required(), validators.length(min=4, max=40)])
    permissions = SelectMultipleField(
        'Select the permissions',
        choices=[],
        validators=[validators.data_required()],
        coerce=int  # Convert the choices keys into int
    )
    submit = SubmitField('Submit')


class BindRolesWithUserForm(FlaskForm):
    user = SelectField(
        'Select the user',
        choices=[],
        validators=[validators.data_required()],
        coerce=int
    )
    roles = SelectMultipleField(
        'Select the roles',
        choices=[],
        validators=[validators.data_required()],
        coerce=int  # Convert the choices keys into int
    )
    submit = SubmitField('Submit')
