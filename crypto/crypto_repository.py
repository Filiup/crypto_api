from sqlalchemy.exc import IntegrityError
from crypto.expecptions.database import DatabaseException
from crypto.models.cryto_currency_model import CryptoCurrencyModel
from sqlalchemy import select
from sqlalchemy.orm import Session

class CryptoRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, model):
        try:
            self.session.add(model)
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise DatabaseException("Crypto currency already exists.")

        return model
    
    def get_many(self):
        return self.session.query(CryptoCurrencyModel).all()
    
    def get_one(self, id: int):
        return self.session.query(CryptoCurrencyModel).where(CryptoCurrencyModel.id == id).first()
    



