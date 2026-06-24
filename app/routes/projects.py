from flask import Blueprint, render_template, redirect, url_for, request, flash
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

        flash("Project created successfully!", "success")

        return redirect(url_for("projects.projects"))

    return render_template("create_project.html", form=form)


@projects_bp.route("/edit/<int:project_id>", methods=["GET", "POST"])
def edit_project(project_id):
    project = Project.query.get_or_404(project_id)
    form = ProjectForm(obj=project)

    if form.validate_on_submit():
        project.name = form.name.data
        project.description = form.description.data
        project.start_date = form.start_date.data
        project.due_date = form.due_date.data
        project.status = form.status.data

        db.session.commit()

        flash("Project updated successfully!", "success")

        return redirect(url_for("projects.projects"))

    return render_template("edit_project.html", form=form, project=project)


@projects_bp.route("/delete/<int:project_id>", methods=["POST"])
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)

    db.session.delete(project)
    db.session.commit()

    flash("Project deleted successfully!", "success")

    return redirect(url_for("projects.projects"))