from typing import override
from sqlalchemy.exc import IntegrityError
from crypto.exceptions.database import DatabaseException
from crypto.models.cryto_currency_model import CryptoCurrencyModel
from db.repository import Repository

class CryptoRepository(Repository[CryptoCurrencyModel]):
    def __init__(self, session):
        super().__init__(session, CryptoCurrencyModel)

    @override
    def create(self, model):
        try:
            super().create(model)
        except IntegrityError:
            self.session.rollback()
            raise DatabaseException("Crypto currency already exists.")
    
        return model


