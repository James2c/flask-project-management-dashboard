from flask import Blueprint, render_template
from app.models.project import Project
from app.models.task import Task

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
def dashboard():
    projects = Project.query.all()

    total_projects = len(projects)
    active_projects = Project.query.filter_by(status="Active").count()
    completed_projects = Project.query.filter_by(status="Completed").count()

    overdue_tasks = [
        task for task in Task.query.all()
        if task.is_overdue()
    ]

    return render_template(
        "dashboard.html",
        total_projects=total_projects,
        active_projects=active_projects,
        completed_projects=completed_projects,
        projects=projects,
        overdue_tasks=overdue_tasks
    )