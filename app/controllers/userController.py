from ..repositories import UserRepository


class UserController:
    def __init__(self):
        self.userRepo = UserRepository()

    def create(self, user):
        return self.userRepo.create(user.dict())
