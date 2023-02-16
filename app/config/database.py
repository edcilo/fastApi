import os

from .types import TDbConfig

db_config: TDbConfig = {
    'default': os.getenv("DB_CONNECTION", "sqlite"),

    'connections': {
        'sqlite': {
            'location': os.getenv("DB_PATH", "sqlite.db"),
        },

        'postgres': {
            "host": os.getenv('DB_HOST', 'localhost'),
            "port": os.getenv('DB_PORT', 5432),
            "database": os.getenv('DB_DATABASE', 'postgres'),
            "user": os.getenv('DB_USER', 'postgres'),
            "password": os.getenv('DB_PASSWORD'),
        },

        'mysql': {
            "host": os.getenv('DB_HOST', 'localhost'),
            "port": os.getenv('DB_PORT', 3306),
            "database": os.getenv('DB_DATABASE', 'mysql'),
            "user": os.getenv('DB_USER', 'mysql'),
            "password": os.getenv('DB_PASSWORD'),
        },
    },
}
