from abc import ABC, abstractmethod, abstractproperty
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Engine(ABC):
    def __init__(self):
        self.base = declarative_base()

    @abstractproperty
    def url(self):
        pass

    def engine(self):
        return create_engine(self.url)

    def session(self):
        return sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine()
        )

    def create_all(self):
        self.base.metadata.create_all(bind=self.engine())

    def drop_all(self):
        self.base.metadata.drop_all(bind=self.engine())
