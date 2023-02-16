from fastapi import APIRouter, Depends, status

from ..controllers import UserController
from ..schemas import UserCreateSchema, UserSchema, UserUpdateSchema

router = APIRouter(prefix="/api/v1/users")


@router.get("/", status_code=status.HTTP_200_OK)
def get_users_route(
        userController=Depends(UserController)) -> list[UserSchema]:
    return userController.all()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user_route(
        user: UserCreateSchema,
        userController=Depends(UserController),) -> UserSchema:
    return userController.create(user)


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_user_route(
        id: int,
        userController=Depends(UserController)) -> UserSchema:
    return userController.detail(id)


@router.put("/{id}", status_code=status.HTTP_200_OK)
def update_user_route(
        id: int,
        user: UserUpdateSchema,
        userController=Depends(UserController)) -> UserSchema:
    return userController.update(id, user)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_route(
        id: int,
        userController=Depends(UserController)) -> None:
    return userController.delete(id)
