from crypto.models.cryto_currency_model import CryptoCurrencyModel
from db.repository import Repository

class CryptoRepository(Repository):
    def create(self, obj):
        pass

    def read(self, model, obj_id):
        pass
    
    def update(self, obj: CryptoCurrencyModel):
        pass

    def delete(self, obj):
        pass


