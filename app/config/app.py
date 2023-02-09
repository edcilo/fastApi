import os
from .types import TAppConfig


app_config: TAppConfig = {
    'app': {
        'name': os.getenv('APP_NAME', 'FastAPI'),
        'version': os.getenv('APP_VERSION', '1.0.0'),
    },

    'cors': {
        'origins': [
            'http://localhost'
        ],
        'methods': ['*'],
        'headers': ['*'],
    }
}
