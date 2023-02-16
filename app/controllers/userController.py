from fastapi import HTTPException

from ..repositories import UserRepository


class UserController:
    def __init__(self):
        self.userRepo = UserRepository()

    def all(self):
        return self.userRepo.all()

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
