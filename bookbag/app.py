from flask import Flask
from bookbag.settings import DevConfig
from bookbag.extensions import cors
from bookbag import resource_claims


def create_app(app_config=DevConfig):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config)
    origins = app.config.get('origins', '*')
    cors.init_app(app, origins=origins)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    return app


def register_blueprints(app):
    app.register_blueprint(resource_claims.views.blueprint)
