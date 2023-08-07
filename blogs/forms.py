from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, Form, FieldList, FormField, StringField
from wtforms import validators


class CommentForm(Form):
    body = TextAreaField(
        'Body', 
        validators = [validators.DataRequired()]
    )


class PostForm(FlaskForm):
    title = StringField(
        'Title', 
        validators=[
            validators.DataRequired(),
            validators.Length(min=1, max=255)
        ]
    )
    body = TextAreaField(
        'Body',
        validators=[
            validators.DataRequired(),
            validators.Length(min=1)
        ]
    )
    comments = FieldList(FormField(CommentForm))
    submit = SubmitField('Submit')
