from ..repositories import UserRepository


class UserController:
    def __init__(self):
        self.userRepo = UserRepository()

    def create(self, user):
        user = self.userRepo.create(user.dict())
        return {
            "id": user.id,
            "email": user.email,
            "password": user.password,
        }
