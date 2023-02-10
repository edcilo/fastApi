from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .engine import Engine


class SQLite(Engine):
    prefix = 'sqlite'

    def __init__(self, location: str):
        self.location = location
        self.base = declarative_base()

    def get_url(self):
        return f'{self.prefix}:///{self.location}'

    def engine(self):
        return create_engine(
            self.get_url(),
            connect_args={"check_same_thread": False}
        )

    def session(self):
        return sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine()
        )

    def create_all(self):
        self.base.metadata.create_all(bind=self.engine())
