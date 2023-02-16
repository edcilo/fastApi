from abc import ABCMeta, abstractmethod, abstractproperty

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


class Engine(metaclass=ABCMeta):
    def __init__(self, conn):
        self.conn = conn
        self.dbUrl = self.url(conn)
        self.session = self.session_maker()()

    def __repr__(self):
        return f'(host={self.host}, port={self.port}, database={self.database}))'

    @abstractmethod
    def url(self, conn):
        pass

    @property
    def engine(self):
        return create_engine(url=self.dbUrl)

    def session_maker(self):
        return sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine)

    def commit(self, model=None):
        try:
            self.session.add(model)
            self.session.commit()
            self.session.refresh(model)
            return model
        except Exception as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()

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
        try:
            self.session.delete(model)
            self.session.commit()
            return model
        except Exception as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()
