from flask import Blueprint, render_template, redirect, url_for, request
from app.extensions import db
from app.models.project import Project
from app.forms.project_form import ProjectForm

projects_bp = Blueprint("projects", __name__, url_prefix="/projects")


@projects_bp.route("/", methods=["GET"])
def projects():
    all_projects = Project.query.all()
    return render_template("projects.html", projects=all_projects)


@projects_bp.route("/create", methods=["GET", "POST"])
def create_project():
    form = ProjectForm()

    if form.validate_on_submit():
        new_project = Project(
            name=form.name.data,
            description=form.description.data,
            start_date=form.start_date.data,
            due_date=form.due_date.data,
            status=form.status.data
        )

        db.session.add(new_project)
        db.session.commit()

        return redirect(url_for("projects.projects"))

    return render_template("create_project.html", form=form)