from abc import abstractmethod
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.hybrid import hybrid_property

class Base(DeclarativeBase):
    @hybrid_property
    @abstractmethod
    def identifier(self):
        pass