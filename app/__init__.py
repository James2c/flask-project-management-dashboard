from flask import Flask
from .extensions import db
from .routes.projects import projects_bp


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "dev-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project_dashboard.db"

    db.init_app(app)

    from app.models import Project

    from .routes.dashboard import dashboard_bp
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(projects_bp)

    return app