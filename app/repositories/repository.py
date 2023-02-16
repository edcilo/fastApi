from abc import ABC, abstractproperty
from typing import Union

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

    def all(
            self,
            order_column: str = "created_at",
            order: str = 'desc') -> list[Model]:
        column = getattr(self.model, order_column)
        order_by = getattr(column, order)
        q = self.query.order_by(order_by())
        return q.all()

    def paginate(
            self,
            order_column: str = "created_at",
            order: str = 'desc',
            page: int = 1,
            per_page: int = 15) -> list[Model]:
        skip = (page - 1) * per_page
        column = getattr(self.model, order_column)
        order_by = getattr(column, order)
        q = self.query.order_by(order_by())
        list = q.limit(per_page).offset(skip).all()
        total = q.count()
        return {
            "data": list,
            "pagination": {
                "page": page,
                "per_page": per_page,
                "prev": page - 1 if page > 1 else None,
                "next": page + 1 if page * per_page < total else None,
                "total": total,
            }
        }

    def create(self, data: dict) -> Model:
        model = self.model(data)
        return self.db.commit(model)

    def get_by_id(self, id: Union[int, Model]) -> Model:
        if isinstance(id, Model):
            return id
        return self.query.filter_by(id=id).first()

    def update(self, id: Union[int, Model], data: dict) -> Model:
        model = self.get_by_id(id)
        model.update(data)
        return self.db.commit(model)

    def delete(self, id: Union[int, Model]) -> Model:
        model = self.get_by_id(id)
        self.db.delete(model)
        return model
