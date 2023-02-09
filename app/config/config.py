from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .app import app_config
from .types import TAppConfig, TApp, TCors


def setup_app(settings: TAppConfig) -> FastAPI:
    app = setup_app_config(settings.get('app', {}))
    setup_cors_config(app, settings.get('cors', {}))
    return app


def setup_app_config(settings: TApp) -> FastAPI:
    settings = {**app_config.get('app', {}), **settings}
    app = FastAPI(
        title=settings.get('name', 'FastAPI'),
        version=settings.get('version', '1.0.0'),
    )
    return app


def setup_cors_config(app: FastAPI, settings: TCors):
    settings = {**app_config.get('cors', {}), **settings}
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.get('origins', ['*']),
        allow_methods=settings.get('methods', ['*']),
        allow_headers=settings.get('headers', ['*']),
    )
