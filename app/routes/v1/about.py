from fastapi import APIRouter, Request

router = APIRouter(prefix="/api/v1/about")


@router.get("/")
def about_route(request: Request):
    return {
        "name": request.app.title,
        "version": request.app.version,
    }
