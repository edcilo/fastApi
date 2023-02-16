from .engine import Engine


class MySQL(Engine):
    def url(self, conn) -> str:
        return f'mysql://{conn["user"]}:{conn["password"]}@{conn["host"]}:{conn["port"]}/{conn["database"]}'
