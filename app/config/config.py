import logging
from functools import lru_cache

from mergedeep import merge
from pydantic import BaseSettings

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .app import app_config
from .database import db_config
from .types import AppSchema, DBSchema, TApp, TConfig, TCors


class SettingsSchema(BaseSettings):
    app: AppSchema = app_config
    db: DBSchema = db_config


@lru_cache()
def get_settings():
    return SettingsSchema()


def get_settings_override(settings: TConfig):
    return SettingsSchema(**settings)


def setup_app(settings: TConfig) -> FastAPI:
    settings = merge({'app': app_config, 'db': db_config}, settings)
    setup_log_config(settings.get('app'))
    app = setup_app_config(settings.get('app').get('app', {}))
    setup_cors_config(app, settings.get('app').get('cors', {}))
    app.dependency_overrides[get_settings] = get_settings_override(settings)
    logging.info(msg='App initialized')
    return app


def setup_log_config(settings: TApp):
    log_level = settings.get('log_level', 'INFO')
    logging.basicConfig(
        level=logging.getLevelName(level=log_level),
        format="%(asctime)s %(levelname)-8s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logging.info('Logging configured')


def setup_app_config(settings: TApp) -> FastAPI:
    app = FastAPI(
        title=settings.get('name', 'FastAPI'),
        version=settings.get('version', '1.0.0'),
    )
    logging.info(msg='App configured')
    return app


def setup_cors_config(app: FastAPI, settings: TCors):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.get('origins', ['*']),
        allow_methods=settings.get('methods', ['*']),
        allow_headers=settings.get('headers', ['*']),
    )
    logging.info('CORS configured')
