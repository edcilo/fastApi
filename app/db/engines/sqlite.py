from .engine import Engine


class SQLite(Engine):
    def __init__(self, location: str):
        super().__init__()
        self.location = location

    @property
    def url(self):
        return f'sqlite:///{self.location}'

    def engine(self):
        return create_engine(
            self.url,
            connect_args={"check_same_thread": False}
        )
