from .engine import Engine


class MySQL(Engine):
    @property
    def url(self):
        return f'mysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'
