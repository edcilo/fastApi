from fastapi import APIRouter, Depends

from ..controllers import UserController
from ..schemas import UserCreateSchema

router = APIRouter(prefix="/api/v1/users")


@router.post("/")
def create_user_route(
    user: UserCreateSchema,
    userController=Depends(UserController),
):
    return userController.create(user)
