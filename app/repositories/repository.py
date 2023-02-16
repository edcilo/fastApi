from abc import ABC, abstractproperty

from ..db import db
from ..models import Model


class Repository(ABC):
    def __init__(self):
        self.db = db

    @abstractproperty
    def model(self) -> Model:
        pass

    @property
    def query(self):
        return self.db.session.query(self.model)

    def all(self,
            order_column="created_at",
            order='desc',
            paginate=False,
            page=1,
            per_page=15):
        column = getattr(self.model, order_column)
        order_by = getattr(column, order)
        q = self.query.order_by(order_by())
        return q.all()

    def create(self, data):
        model = self.model(data)
        return self.db.commit(model)

    def detail(self, id):
        if isinstance(id, Model):
            return id
        return self.query.filter_by(id=id).first()

    def update(self, id, data):
        model = self.detail(id)
        model.update(data)
        self.db.commit(model)
        return model

    def delete(self, id):
        model = self.detail(id)
        self.db.delete(model)
        return model
