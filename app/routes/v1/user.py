from fastapi import APIRouter, Depends, status

from ...controllers import UserController
from ...schemas import (
    UserCreateSchema, UserPaginationSchema, UserSchema, UserUpdateSchema
)
from ...schemas.commonSchema import PaginationParamsSchema

router = APIRouter(prefix="/api/v1/users")


@router.get("/", status_code=status.HTTP_200_OK)
def get_paginated_users_route(
        order_column: str = 'created_at',
        order: str = 'desc',
        page: int = 1,
        per_page: int = 15,
        userController=Depends(UserController)) -> UserPaginationSchema:
    return userController.paginate({
        'order_column': order_column,
        'order': order,
        'page': page,
        'per_page': per_page
    })


@ router.get("/list", status_code=status.HTTP_200_OK)
def get_all_users_route(
        userController=Depends(UserController)) -> list[UserSchema]:
    return userController.all()


@ router.post("/", status_code=status.HTTP_201_CREATED)
def create_user_route(
        user: UserCreateSchema,
        userController=Depends(UserController),) -> UserSchema:
    return userController.create(user)


@ router.get("/{id}", status_code=status.HTTP_200_OK)
def get_user_route(
        id: int,
        userController=Depends(UserController)) -> UserSchema:
    return userController.detail(id)


@ router.put("/{id}", status_code=status.HTTP_200_OK)
def update_user_route(
        id: int,
        user: UserUpdateSchema,
        userController=Depends(UserController)) -> UserSchema:
    return userController.update(id, user)


@ router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_route(
        id: int,
        userController=Depends(UserController)) -> None:
    return userController.delete(id)
