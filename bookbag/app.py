from flask import Flask, g
from bookbag.settings import DevConfig
from bookbag.extensions import cors
from bookbag.transport import resource_claims
from bookbag.config import FakedConfig, BaseConfig
import os


def create_app(app_config=DevConfig):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config)
    origins = app.config.get('origins', '*')
    cors.init_app(app, origins=origins)
    register_extensions(app)
    register_blueprints(app)
    if os.environ.get('FLASK_DEBUG') == '1':
        app.config.from_object(FakedConfig)
    else:
        app.config.from_object(BaseConfig)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    return app


def register_blueprints(app):
    app.register_blueprint(resource_claims)
