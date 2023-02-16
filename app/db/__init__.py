from ..config.config import get_settings
from .engines import engineFactory


def setup_db():
    db_settings = get_settings().db
    default = db_settings.default
    connection = getattr(db_settings.connections, default)
    return engineFactory(
        engineName=default,
        settings=connection.dict())


db = setup_db()
