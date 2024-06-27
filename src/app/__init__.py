from flask import Flask

def register_blueprints(app: Flask) -> None:
    from .routes import app_routes

    app.register_blueprint(app_routes)

def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)

    return app