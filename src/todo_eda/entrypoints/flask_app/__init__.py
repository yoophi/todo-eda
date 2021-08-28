from flask import Flask


def init_bp(app: Flask):
    from todo_eda.entrypoints.flask_app.views.api import api as api_bp

    app.register_blueprint(api_bp, url_prefix='/api')


def create_app():
    app = Flask(__name__)
    init_bp(app)

    return app
