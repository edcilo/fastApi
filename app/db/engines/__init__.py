from ...config.config import get_settings


def engineFactory():
    db_settings = get_settings().db
    engineName = db_settings.default
    engines_settings = db_settings.connections.dict()
    settings = engines_settings.get(engineName)
    if engineName == 'sqlite':
        from .sqlite import SQLite as engine
    elif engineName == 'psql':
        from .psql import PSQL as engine
    elif engineName == 'mysql':
        from .mysql import MySQL as engine
    else:
        raise Exception('Unknown engine: %s' % engineName)

    return engine(**settings)
