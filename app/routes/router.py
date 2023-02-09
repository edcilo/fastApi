from fastapi import FastAPI
from . import about


def setup_routes(app: FastAPI):
    app.include_router(about.router)
