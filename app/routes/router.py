from . import about


def setup_routes(app):
    app.include_router(about.router)
