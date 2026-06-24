from flask import Blueprint, render_template
from app.models.project import Project

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
def dashboard():
    projects = Project.query.all()

    total_projects = len(projects)
    active_projects = Project.query.filter_by(status="Active").count()
    completed_projects = Project.query.filter_by(status="Completed").count()

    return render_template(
        "dashboard.html",
        total_projects=total_projects,
        active_projects=active_projects,
        completed_projects=completed_projects,
        projects=projects
    )