from ..db import db
from .model import Base, Model
from .user import User


def create_tables():
    Base.metadata.create_all(bind=db.engine)
