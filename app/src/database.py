from flask_sqlalchemy import SQLAlchemy
from app.core.models import BaseModel


db = SQLAlchemy(model_class=BaseModel)


def configure_db(app):
    db.init_app(app)
    app.db = db
