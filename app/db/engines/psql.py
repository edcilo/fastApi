from .engine import Engine


class PSQL(Engine):
    def __init__(self, host: str, port: int, username: str, password: str, database: str):
        super().__init__()
        self.host = host
        self.port = port
        self.user = username
        self.password = password
        self.database = database

    @property
    def url(self):
        return f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'
