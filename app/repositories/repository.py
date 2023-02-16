from abc import ABC, abstractproperty

from ..db import db


class Repository(ABC):
    def __init__(self):
        self.db = db

    @abstractproperty
    def model(self):
        pass

    def create(self, data):
        model = self.model(data)
        model = self.db.commit(model)
        return model
