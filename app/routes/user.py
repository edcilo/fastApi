from fastapi import APIRouter, Depends

from ..controllers import UserController
from ..schemas import UserCreateSchema, UserUpdateSchema

router = APIRouter(prefix="/api/v1/users")


@router.get("/")
def get_users_route(
        userController=Depends(UserController)):
    return userController.all()


@router.post("/")
def create_user_route(
        user: UserCreateSchema,
        userController=Depends(UserController),):
    return userController.create(user)


@router.get("/{id}")
def get_user_route(
        id: int,
        userController=Depends(UserController)):
    return userController.detail(id)


@router.put("/{id}")
def update_user_route(
        id: int,
        user: UserUpdateSchema,
        userController=Depends(UserController)):
    return userController.update(id, user)


@router.delete("/{id}")
def delete_user_route(
        id: int,
        userController=Depends(UserController)):
    return userController.delete(id)
