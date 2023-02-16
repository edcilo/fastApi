from fastapi import HTTPException, Request, status

from ..decorators import getEntity, validator
from ..models import User
from ..repositories import UserRepository
from ..schemas import (
    UserCreateSchema, UserListAllParamsSchema, UserPaginationParamsSchema,
    UserUpdateSchema
)


class UserController:
    def __init__(self, request: Request):
        self.request = request
        self.userRepo = UserRepository()

    @validator(UserListAllParamsSchema)
    def all(self, params) -> list[User]:
        return self.userRepo.all(**params.dict())

    @validator(UserPaginationParamsSchema)
    def paginate(self, params):
        return self.userRepo.paginate(**params.dict())

    def create(self, params: UserCreateSchema) -> User:
        return self.userRepo.create(params)

    @getEntity(UserRepository)
    def detail(self, user: User) -> User:
        return user

    @getEntity(UserRepository)
    def update(self, user: User, params: UserUpdateSchema) -> User:
        return self.userRepo.update(user, params)

    @getEntity(UserRepository)
    def delete(self, user: User) -> User:
        return self.userRepo.delete(user)
