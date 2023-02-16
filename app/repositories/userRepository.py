from ..models import User
from .repository import Repository


class UserRepository(Repository):
    @property
    def model(self):
        return User
