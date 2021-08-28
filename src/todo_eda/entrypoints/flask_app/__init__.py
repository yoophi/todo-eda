from flask import Flask
from flask_cors import CORS


def init_bp(app: Flask):
    from todo_eda.entrypoints.flask_app.views.api import api as api_bp

    app.register_blueprint(api_bp, url_prefix="/api")


def init_extensions(app):
    pass
    # cors = CORS(
    #     app,
    #     resources={r"/api/*": {"origins": "*"}})


def create_app():
    app = Flask(__name__)
    init_extensions(app)
    init_bp(app)

    return app
