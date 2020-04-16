from flask import Flask, g
from bookbag.settings import DevConfig
from bookbag.extensions import cors
from bookbag.transport import resource_claims, resources
from bookbag.config import FakedConfig, ProductionConfig
from dotenv import load_dotenv
import os

load_dotenv()


def create_app(app_config=DevConfig):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config)
    origins = app.config.get('origins', '*')
    cors.init_app(app, origins=origins)
    register_extensions(app)
    register_blueprints(app)
    if os.environ.get('FLASK_DEBUG') == '1':
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(ProductionConfig)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    return app


def register_blueprints(app):
    app.register_blueprint(resource_claims)
    app.register_blueprint(resources.blueprint)