from fastapi import FastAPI

from .config import config, types
from .routes import router


def new_app(settings={}) -> FastAPI:
    app = config.setup_app(settings)
    router.setup_routes(app)

    # from .models import create_tables
    # create_tables()

    return app


# config = {
#     'db': {
#         'default': 'postgres',
#     }
# }
app = new_app()
