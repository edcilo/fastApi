from abc import ABC, abstractproperty
from ..models import db


class Repository(ABC):
    def __init__(self):
        self.session = db.session()

    @abstractproperty
    def model(self):
        pass

    def save(self, model):
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

    def bulk_save(self, models):
        try:
            self.session.bulk_save_objects(models)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()

    def delete(self, model):
        try:
            self.session.delete(model)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()

    def close(self):
        self.session.close()

    def rollback(self):
        self.session.rollback()

    def create(self, data):
        return self.save(self.model(data))
