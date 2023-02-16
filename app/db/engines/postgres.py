from .engine import Engine


class Postgres(Engine):
    def url(self, conn) -> str:
        return f'postgresql://{conn["user"]}:{conn["password"]}@{conn["host"]}:{conn["port"]}/{conn["database"]}'
