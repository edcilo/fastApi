from ..models import User
from ..schemas import UserCreateSchema
from .repository import Repository


class UserRepository(Repository):
    @property
    def model(self):
        return User
