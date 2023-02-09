from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import router


def new_app():
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            'http://localhost',
        ],
        allow_methods=['*'],
        allow_headers=['*'],
    )

    router.setup_routes(app)

    return app


app = new_app()
