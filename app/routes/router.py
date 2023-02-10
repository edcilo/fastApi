from fastapi import FastAPI
from . import about
from . import user


def setup_routes(app: FastAPI):
    app.include_router(about.router)
    app.include_router(user.router)
