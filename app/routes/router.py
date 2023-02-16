from fastapi import FastAPI

from .v1 import about, user


def setup_routes(app: FastAPI):
    app.include_router(about.router)
    app.include_router(user.router)
