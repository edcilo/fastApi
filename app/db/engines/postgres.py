from .engine import Engine


class Postgres(Engine):
    @property
    def url(self):
        return f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'
