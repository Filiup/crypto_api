from xxlimited import Str
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Database:
    def __init__(self, url: str):
        self.db = sa.create_engine(url, echo=True)
        self.Session = sessionmaker(bind=self.db)

    def get_session(self):
        return self.Session()