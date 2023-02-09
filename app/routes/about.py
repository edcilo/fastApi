from fastapi import APIRouter


router = APIRouter(
    prefix="/api/v1/about",
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def about_route():
    return {"message": "About page"}
