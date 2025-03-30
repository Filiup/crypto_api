from os import name
from crypto.crypto_repository import CryptoRepository
from crypto.dto.create_crypto import CreateCryptoDto
from crypto.models.cryto_currency_model import CryptoCurrencyModel
from db import repository

class CryptoService:
    def __init__(self, repository: CryptoRepository):
        self.repository = repository

    def test(self):
        return "hello !!!!"
    
    def getCurerency(self, obj_id):
        return self.repository.read(CryptoCurrencyModel, obj_id)
    
    def createCurrency(self, dto: CreateCryptoDto):
        crypto_currency_model = CryptoCurrencyModel(
            name=dto.name,
            symbol=dto.symbol,
            coingecko_id=dto.coingecko_id
        )

        return self.repository.create(crypto_currency_model)
    


    