from ..repositories import UserRepository


class UserController:
    def __init__(self):
        self.userRepo = UserRepository()

    def all(self):
        return self.userRepo.all()

    def create(self, user):
        return self.userRepo.create(user.dict())

    def detail(self, id):
        return self.userRepo.detail(id)

    def update(self, id, user):
        return self.userRepo.update(id, user.dict())

    def delete(self, id):
        return self.userRepo.delete(id)
