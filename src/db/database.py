import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

class Database:
    def __init__(self, url: str, echo: bool):
        self.db = sa.create_engine(url, echo=echo)
        self.Session = sessionmaker(bind=self.db)

    def get_new_session(self):
        return self.Session()

    def __enter__(self):
        self.session = self.get_new_session()
        return self.session

    def __exit__(self, exc_type, exc_value, traceback):
        if self.session:
            self.session.close()