from flask import Blueprint, render_template

projects_bp = Blueprint(
    "projects",
    __name__,
    url_prefix="/projects"
)


@projects_bp.route("/")
def projects():
    return render_template("projects.html")