from flask import Flask
from flask_migrate import Migrate

from .src.database import configure_db


def create_app():
    app = Flask(__name__)

    app.config.from_object('config.Development')

    configure_db(app)

    Migrate(app, app.db)

    return app


app = create_app()
