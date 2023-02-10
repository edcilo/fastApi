import sqlalchemy as sa
from .model import Model


class User(Model):
    __tablename__ = "users"

    _fillable = ("email", "password",)

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    email = sa.Column(sa.String, unique=True, index=True)
    password = sa.Column(sa.String)
    is_active = sa.Column(sa.Boolean, default=True)
