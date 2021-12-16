from datetime import datetime

from flask_sqlalchemy import Model
from flask_sqlalchemy.model import sa
from sqlalchemy.ext.declarative import declared_attr


class BaseModel(Model):
    criado_em = sa.Column(sa.DateTime, default=datetime.now)
    atualizado_em = sa.Column(sa.DateTime, default=datetime.now, onupdate=datetime.now)

    @declared_attr
    def id(cls):
        for base in cls.__mro__[1:-1]:
            if getattr(base, '__table__', None) is not None:
                type = sa.ForeignKey(base.id)
                break
        else:
            type = sa.Integer

        return sa.Column(type, primary_key=True)
