from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import config, types
from .routes import router


def new_app(settings: types.TAppConfig = {}) -> FastAPI:
    app = config.setup_app(settings)
    router.setup_routes(app)
    return app


app = new_app()
