from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import config, types
from .routes import router
# TODO: just for testing
from .models import db


def new_app(settings: types.TAppConfig = {}) -> FastAPI:
    app = config.setup_app(settings)
    router.setup_routes(app)
    # TODO: just for testing
    db.create_all()
    return app


app = new_app()
