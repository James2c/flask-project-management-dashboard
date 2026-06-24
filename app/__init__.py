from flask import Flask
from .extensions import db


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "dev-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project_dashboard.db"

    db.init_app(app)

    from .routes.dashboard import dashboard_bp
    app.register_blueprint(dashboard_bp)

    return app