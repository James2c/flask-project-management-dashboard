from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SelectField
from wtforms.validators import DataRequired, Length


class ProjectForm(FlaskForm):
    name = StringField("Project Name", validators=[DataRequired(), Length(max=100)])

    description = TextAreaField("Description")

    start_date = DateField("Start Date", format="%Y-%m-%d", validators=[DataRequired()])

    due_date = DateField("Due Date", format="%Y-%m-%d", validators=[DataRequired()])

    status = SelectField(
        "Status",
        choices=[
            ("Active", "Active"),
            ("Completed", "Completed"),
            ("On Hold", "On Hold")
        ]
    )