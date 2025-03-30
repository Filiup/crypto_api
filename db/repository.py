from sqlalchemy.orm import Session
from abc import ABC, abstractmethod

class Repository(ABC):
    def __init__(self, session: Session):
        self.session = session

    def create(self, model):
        self.session.add(model)
        self.session.commit()

        return model

    @abstractmethod
    def read(self, model, obj_id):
        pass
    
    @abstractmethod
    def update(self, obj):
        pass

    @abstractmethod
    def delete(self, obj):
        pass