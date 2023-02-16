def engineFactory(engineName, settings):
    if engineName == 'sqlite':
        from .sqlite import SQLite as Engine
    elif engineName == 'postgres':
        from .postgres import Postgres as Engine
    elif engineName == 'mysql':
        from .mysql import MySQL as Engine
    else:
        raise Exception('Unknown engine: %s' % engineName)

    return Engine(conn=settings)
