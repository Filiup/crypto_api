from sqlalchemy.orm import Session
from abc import ABC, abstractmethod

class Repository(ABC):
    def __init__(self, session: Session):
        self.session = session

    @abstractmethod
    def create(self, obj):
        pass

    @abstractmethod
    def read(self, model, obj_id):
        pass
    
    @abstractmethod
    def update(self, obj):
        pass

    @abstractmethod
    def delete(self, obj):
        pass