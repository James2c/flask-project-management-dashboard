import os
from flask import Flask
from .extensions import db


class Config:
    SECRET_KEY = "dev-key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///project_dashboard.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from app.models import Project

    from .routes.dashboard import dashboard_bp
    from .routes.projects import projects_bp

    app.register_blueprint(dashboard_bp)
    app.register_blueprint(projects_bp)

    return app