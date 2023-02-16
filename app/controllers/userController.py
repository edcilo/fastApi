from fastapi import HTTPException, status

from ..repositories import UserRepository
from ..schemas import UserPaginationParamsSchema


class UserController:
    def __init__(self):
        self.userRepo = UserRepository()

    def all(self):
        return self.userRepo.all()

    def paginate(self, params):
        try:
            params = UserPaginationParamsSchema(**params)
            return self.userRepo.paginate(**params.dict())
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=e.errors())

    def create(self, user):
        return self.userRepo.create(user.dict())

    def detail(self, id):
        user = self.userRepo.detail(id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def update(self, id, user):
        return self.userRepo.update(id, user.dict())

    def delete(self, id):
        return self.userRepo.delete(id)
