from app.extensions import db


class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    description = db.Column(db.Text)

    start_date = db.Column(db.Date)

    due_date = db.Column(db.Date)

    tasks = db.relationship("Task", backref="project", cascade="all, delete-orphan")

    status = db.Column(
        db.String(20),
        nullable=False,
        default="Active"
    )

    def __repr__(self):
        return f"<Project {self.name}>"
    
    def progress(self):
        total_tasks = len(self.tasks)
        if total_tasks == 0:
            return 0

        completed_tasks = len([t for t in self.tasks if t.status == "Done"])

        return round((completed_tasks / total_tasks) * 100)