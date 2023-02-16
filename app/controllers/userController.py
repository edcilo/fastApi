from fastapi import HTTPException, Request, status

from ..decorators import getEntity, validator
from ..repositories import UserRepository
from ..schemas import UserListAllParamsSchema, UserPaginationParamsSchema


class UserController:
    def __init__(self, request: Request):
        self.request = request
        self.userRepo = UserRepository()

    @validator(UserListAllParamsSchema)
    def all(self, params):
        return self.userRepo.all(**params.dict())

    @validator(UserPaginationParamsSchema)
    def paginate(self, params):
        return self.userRepo.paginate(**params.dict())

    def create(self, params):
        return self.userRepo.create(params.dict())

    @getEntity(UserRepository)
    def detail(self, user):
        return user

    @getEntity(UserRepository)
    def update(self, user, params):
        return self.userRepo.update(user, params.dict())

    @getEntity(UserRepository)
    def delete(self, user):
        return self.userRepo.delete(user)
