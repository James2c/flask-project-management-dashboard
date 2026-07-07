from app.forms.task_form import TaskForm
from app.models.task import Task
from app.extensions import db
from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models.project import Project
from app.forms.project_form import ProjectForm


projects_bp = Blueprint("projects", __name__, url_prefix="/projects")


@projects_bp.route("/", methods=["GET"])
def projects():
    search = request.args.get("search", "").strip()

    if search:
        all_projects = (
            Project.query
            .filter(Project.name.ilike(f"%{search}%"))
            .all()
        )
    else:
        all_projects = Project.query.all()

    return render_template(
        "projects.html",
        projects=all_projects,
        search=search
    )


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


@projects_bp.route("/<int:project_id>", methods=["GET", "POST"])
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    form = TaskForm()

    if form.validate_on_submit():
        new_task = Task(
            title=form.title.data,
            description=form.description.data,
            status=form.status.data,
            priority=form.priority.data,
            due_date=form.due_date.data,
            project_id=project.id
        )

        db.session.add(new_task)
        db.session.commit()

        return redirect(f"/projects/{project.id}")

    return render_template(
        "project_detail.html",
        project=project,
        form=form
    )


@projects_bp.route("/tasks/<int:task_id>/toggle", methods=["POST"])
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)

    if task.status == "Done":
        task.status = "To Do"
    else:
        task.status = "Done"

    db.session.commit()

    return redirect(url_for("projects.project_detail", project_id=task.project_id))


@projects_bp.route("/tasks/<int:task_id>/delete", methods=["POST"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)

    project_id = task.project_id

    db.session.delete(task)
    db.session.commit()

    return redirect(url_for("projects.project_detail", project_id=project_id))