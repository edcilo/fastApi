from sqlalchemy import create_engine

from .engine import Engine


class SQLite(Engine):
    def __repr__(self):
        return f'(location={self.location})'

    def url(self, conn) -> str:
        return f'sqlite:///{conn["location"]}'

    @property
    def engine(self):
        return create_engine(
            url=self.dbUrl,
            connect_args={"check_same_thread": False}
        )
