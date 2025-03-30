from crypto.coingecko.coingecko_client import CoinGeckoClient
from crypto.crypto_repository import CryptoRepository
from crypto.dto.create_crypto import CreateCryptoDto
from crypto.expecptions.coingecko import CoingeckoException
from crypto.expecptions.crypto_not_found import CryptoNotFoundExpection
from crypto.models.cryto_currency_model import CryptoCurrencyModel

class CryptoService:
    def __init__(self, repository: CryptoRepository, coingecko_client: CoinGeckoClient):
        self.repository = repository
        self.coingecko_client = coingecko_client

    def _find_coingecko_id(self, name: str, symbol: str):
        same_name_symbol = lambda ro: ro['name'] == name and ro['symbol'] == symbol

        coins = self.coingecko_client.get_all_coins()
        coins = filter(same_name_symbol, coins)
        coin: dict = next(coins, {})

        return coin.get("id")


    def getAllCurrencies(self):
        return self.repository.get_many()
    
    def getCryptoCurrency(self, id: int):
        crypto_currency = self.repository.get_one(id)
        if crypto_currency is None:
            raise CryptoNotFoundExpection(f"Coin with id {id} was not found")
        
        return crypto_currency
    
    def deleteCryptoCurrency(self, id: int):
        crypto_currency = self.getCryptoCurrency(id)
        return self.repository.delete_one(crypto_currency)


    def createCurrency(self, dto: CreateCryptoDto):
        coingecko_id = self._find_coingecko_id(dto.name, dto.symbol)
        if coingecko_id is None:
            raise CoingeckoException(f"Coin with name {dto.name} and symbol {dto.symbol} does not exist")

        coin_data = self.coingecko_client.get_coin_by_id(coingecko_id)

        crypto_currency_model = CryptoCurrencyModel(
            name=dto.name,
            symbol=dto.symbol,
            hashing_algorithm=coin_data["hashing_algorithm"],
            categories=coin_data["categories"],
            coingecko_id=coingecko_id
        )

        return self.repository.create(crypto_currency_model)
    


    