from crypto.models.cryto_currency_model import CryptoCurrencyModel
from sqlalchemy.orm import Session

class CryptoRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, model):
        self.session.add(model)
        self.session.commit()

        return model
    
    def get_many(self):
        return self.session.query(CryptoCurrencyModel).all()
    



