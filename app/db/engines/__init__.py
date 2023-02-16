def engineFactory(engineName, settings):
    if engineName == 'sqlite':
        from .sqlite import SQLite as engine
    elif engineName == 'postgres':
        from .postgres import Postgres as engine
    elif engineName == 'mysql':
        from .mysql import MySQL as engine
    else:
        raise Exception('Unknown engine: %s' % engineName)

    return engine(**settings)
