from app.extensions import db
from datetime import date


class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(150), nullable=False)

    description = db.Column(db.Text)

    status = db.Column(
        db.String(20),
        nullable=False,
        default="To Do"
    )

    priority = db.Column(
        db.String(20),
        nullable=False,
        default="Medium"
    )

    due_date = db.Column(db.Date)

    project_id = db.Column(
        db.Integer,
        db.ForeignKey("projects.id"),
        nullable=False
    )

    def __repr__(self):
        return f"<Task {self.title}>"
    

    def is_overdue(self):
        if not self.due_date:
            return False

        if self.status == "Done":
            return False

        return self.due_date < date.today()