from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateField
from wtforms.validators import DataRequired, Length


class TaskForm(FlaskForm):
    title = StringField("Task Title", validators=[DataRequired(), Length(max=150)])

    description = TextAreaField("Description")

    status = SelectField(
        "Status",
        choices=[
            ("To Do", "To Do"),
            ("In Progress", "In Progress"),
            ("Done", "Done")
        ]
    )

    priority = SelectField(
        "Priority",
        choices=[
            ("Low", "Low"),
            ("Medium", "Medium"),
            ("High", "High")
        ]
    )

    due_date = DateField("Due Date", format="%Y-%m-%d")