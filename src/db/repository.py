from typing import TypeVar, Generic, Type, Sequence, Optional
from .base_model import Base
from sqlalchemy.orm import Session

T = TypeVar("T", bound=Base)

class Repository(Generic[T]):
    def __init__(self, session: Session, model: Type[T]):
        self.session = session
        self.model = model

    def create(self, model: T) -> T:
        self.session.add(model)
        self.session.commit()

        return model
    
    def get_many(self) -> Sequence[T]:
        return self.session.query(self.model).all()
    
    def get_one_by(self, stmt) -> Optional[T]:
        return self.session.scalars(stmt).first()
    
    def get_many_by(self, stmt) -> Sequence[T]:
        return self.session.scalars(stmt).all()
    
    def get_one(self, identifier) -> Optional[T]:
        return self.session.query(self.model).where(self.model.identifier == identifier).first()
    
    def delete_one(self, model: T) -> T:
        self.session.delete(model)
        self.session.commit()

        return model


