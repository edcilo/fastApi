import datetime
from typing import Union

import sqlalchemy as sa
from pydantic import BaseModel as PydanticModel
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Model(Base):
    __abstract__ = True

    _fillable = tuple()

    def __init__(self, data=None):
        if data is not None:
            self.setAttrs(data)

    def __repr__(self):
        return f"<{self.__tablename__} id={self.id}>"

    created_at = sa.Column(
        sa.DateTime,
        default=datetime.datetime.utcnow,
        server_default=sa.func.now(),
        nullable=False)

    updated_at = sa.Column(
        sa.DateTime,
        default=datetime.datetime.utcnow,
        server_default=sa.func.now(),
        onupdate=datetime.datetime.utcnow,
        nullable=False)

    def setAttrs(self, data: Union[dict, PydanticModel]):
        if isinstance(data, PydanticModel):
            data = data.dict()
        for attr, value in data.items():
            if attr in self._fillable:
                setattr(self, attr, value)

    def update(self, data: Union[dict, PydanticModel]):
        self.setAttrs(data)
