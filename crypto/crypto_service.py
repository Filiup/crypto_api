from crypto.crypto_repository import CryptoRepository
from crypto.dto.create_crypto import CreateCryptoDto
from crypto.models.cryto_currency_model import CryptoCurrencyModel

class CryptoService:
    def __init__(self, repository: CryptoRepository):
        self.repository = repository

    def getAllCurrencies(self):
        return self.repository.get_many()
    
    def createCurrency(self, dto: CreateCryptoDto):
        crypto_currency_model = CryptoCurrencyModel(
            name=dto.name,
            symbol=dto.symbol,
            coingecko_id=dto.coingecko_id
        )

        return self.repository.create(crypto_currency_model)
    


    