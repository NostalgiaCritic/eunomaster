from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_envvar('APP_CONFIG_FILE')

    with app.app_context():
        app.config.from_envvar('APP_CONFIG_FILE')
        # ORM
        db.init_app(app)
        migrate.init_app(app, db)
        from . import models

        # 블루프린트
        from .views import main_views
        app.register_blueprint(main_views.bp)
        
    return app

