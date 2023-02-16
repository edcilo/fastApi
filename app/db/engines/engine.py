from abc import ABCMeta, abstractmethod, abstractproperty

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


class Engine(metaclass=ABCMeta):
    def __init__(self, host: str, port: int, username: str, password: str, database: str):
        self.host = host
        self.port = port
        self.user = username
        self.password = password
        self.database = database

    def __repr__(self):
        return f'(host={self.host}, port={self.port}, database={self.database}))'

    @abstractproperty
    def url(self):
        pass

    @property
    def engine(self):
        return create_engine(
            self.url
        )

    @property
    def session(self):
        return sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine)

    def commit(self, model):
        session = self.session()
        try:
            session.add(model)
            session.commit()
            session.refresh(model)
            return model
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    # def bulk_save(self, models):
    #     try:
    #         self.session.bulk_save_objects(models)
    #         self.session.commit()
    #     except Exception as e:
    #         self.session.rollback()
    #         raise e
    #     finally:
    #         self.session.close()

    def delete(self, model):
        session = self.session()
        try:
            session.delete(model)
            session.commit()
            return model
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
