from sqlalchemy import create_engine

from .engine import Engine


class SQLite(Engine):
    def __init__(self, location: str):
        self.location = location

    def __repr__(self):
        return f'(location={self.location})'

    @property
    def url(self):
        return f'sqlite:///{self.location}'

    @property
    def engine(self):
        return create_engine(
            self.url,
            connect_args={"check_same_thread": False}
        )
