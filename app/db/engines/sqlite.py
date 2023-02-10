from .engine import Engine


class SQLite(Engine):
    def __init__(self, location: str):
        super().__init__()
        self.location = location

    @property
    def url(self):
        return f'sqlite:///{self.location}'
