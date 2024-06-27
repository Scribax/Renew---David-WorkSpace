# app/__init__.py

import os
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from app.config import factory  # Ajustar la importación absoluta

# Load .env file
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()

def create_app() -> Flask:
    # Determinar el entorno (por defecto a 'development')
    config_name = os.getenv('FLASK_ENV') or 'development'
    
    app = Flask(__name__)

    # Cargar configuración basada en el entorno
    config_class = factory(config_name)
    app.config.from_object(config_class)
    config_class.init_app(app)
    
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    @app.shell_context_processor
    def ctx():
        return {
            "app": app,
            'db': db
        }
    
    return app