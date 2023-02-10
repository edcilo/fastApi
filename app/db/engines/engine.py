from abc import ABC, abstractmethod, abstractproperty
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Engine(ABC):
    @abstractproperty
    def url(self):
        pass

    @property
    def base(self):
        return declarative_base()

    @property
    def engine(self):
        return create_engine(self.url)

    @property
    def session(self):
        return sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine
        )

    def create_all(self):
        self.base.metadata.create_all(bind=self.engine)

    def drop_all(self):
        self.base.metadata.drop_all(bind=self.engine)
