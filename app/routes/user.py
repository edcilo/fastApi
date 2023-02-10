from fastapi import APIRouter, Depends
from ..schemas import UserCreateSchema
from ..controllers import UserController


router = APIRouter(prefix="/api/v1/users")


@router.post("/")
def create_user_route(
    user: UserCreateSchema,
    userController = Depends(UserController),
):
    return userController.create(user)
