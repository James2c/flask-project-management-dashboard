from flask import Blueprint, redirect, url_for
from app.extensions import db
from app.models.task import Task


tasks_bp = Blueprint(
    "tasks",
    __name__,
    url_prefix="/tasks"
)


@tasks_bp.route("/<int:task_id>/toggle", methods=["POST"])
def toggle_task(task_id):

    task = Task.query.get_or_404(task_id)

    if task.status == "Done":
        task.status = "To Do"
    else:
        task.status = "Done"

    db.session.commit()

    return redirect(
        url_for(
            "projects.project_detail",
            project_id=task.project_id
        )
    )


@tasks_bp.route("/<int:task_id>/delete", methods=["POST"])
def delete_task(task_id):

    task = Task.query.get_or_404(task_id)

    project_id = task.project_id

    db.session.delete(task)
    db.session.commit()

    return redirect(
        url_for(
            "projects.project_detail",
            project_id=project_id
        )
    )