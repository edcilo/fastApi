from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from functools import lru_cache
from mergedeep import merge
from pydantic import BaseSettings
from .app import app_config
from .database import db_config
from .types import TConfig, TApp, TCors, AppSchema, DBSchema


class SettingsSchema(BaseSettings):
    app: AppSchema = app_config
    db: DBSchema = db_config


@lru_cache()
def get_settings():
    return SettingsSchema()


def get_settings_override(settings: TConfig):
    return SettingsSchema(**settings)


def setup_app(settings: TConfig) -> FastAPI:
    settings = merge({
        'app': app_config,
        'db': db_config,
    }, settings)
    app = setup_app_config(settings.get('app').get('app', {}))
    setup_cors_config(app, settings.get('app').get('cors', {}))
    app.dependency_overrides[get_settings] = get_settings_override(settings)
    return app


def setup_app_config(settings: TApp) -> FastAPI:
    app = FastAPI(
        title=settings.get('name', 'FastAPI'),
        version=settings.get('version', '1.0.0'),
    )
    return app


def setup_cors_config(app: FastAPI, settings: TCors):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.get('origins', ['*']),
        allow_methods=settings.get('methods', ['*']),
        allow_headers=settings.get('headers', ['*']),
    )
