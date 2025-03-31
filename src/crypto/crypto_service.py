from typing import List
from datetime import datetime
from crypto.coingecko.coingecko_client import CoinGeckoClient
from crypto.coingecko.types import CoinDataResponse
from crypto.crypto_repository import CryptoRepository
from crypto.dto.create_crypto import CreateCryptoDto
from crypto.dto.crypto_query import CryptoQueryDto
from crypto.dto.put_crypto import PutCryptoDto
from crypto.exceptions.coingecko import CoingeckoException
from crypto.models.cryto_currency_model import CryptoCurrencyModel
from sqlalchemy import select

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

    def get_currencies(self, dto: CryptoQueryDto):
        stmt = select(CryptoCurrencyModel)

        if dto.category is not None:
            stmt = stmt.where(CryptoCurrencyModel.categories.any(dto.category))

        if dto.coingecko_id is not None:
            stmt = stmt.where(CryptoCurrencyModel.coingecko_id == dto.coingecko_id)

        if dto.name is not None:
            stmt = stmt.where(CryptoCurrencyModel.name == dto.name)

        if dto.symbol is not None:
            stmt = stmt.where(CryptoCurrencyModel.symbol == dto.symbol)

        return self.repository.get_many_by(stmt)
    
    def get_currency(self, id: int):
        crypto_currency = self.repository.get_one(id)
        return crypto_currency
    
    def delete_currency(self, model: CryptoCurrencyModel):
        deleted_currency = self.repository.delete_one(model)
        return deleted_currency


    def create_currency(self, dto: CreateCryptoDto):
        coingecko_id = self._find_coingecko_id(dto.name, dto.symbol)
        if coingecko_id is None:
            raise CoingeckoException(f"Coin with name {dto.name} and symbol {dto.symbol} does not exist")

        coin_data = self.coingecko_client.get_coin_by_id(coingecko_id)

        crypto_currency_model = CryptoCurrencyModel(
            name=dto.name,
            symbol=dto.symbol,
            hashing_algorithm=coin_data.hashing_algorithm,
            categories=coin_data.categories,
            current_price=coin_data.current_price,
            market_cap=coin_data.market_cap,
            total_supply=coin_data.total_supply,
            last_updated=datetime.fromisoformat(coin_data.last_updated.replace("Z", "+00:00")),
            image_url=coin_data.image_url,
            coingecko_id=coingecko_id
        )

        return self.repository.create(crypto_currency_model)
    
    def update_currency(self, model: CryptoCurrencyModel, coin_data: CoinDataResponse):
        model.name = coin_data.name
        model.symbol = coin_data.symbol
        model.current_price=coin_data.current_price,
        model.market_cap=coin_data.market_cap,
        model.total_supply=coin_data.total_supply,
        model.last_updated=datetime.fromisoformat(coin_data.last_updated.replace("Z", "+00:00")),
        model.image_url=coin_data.image_url,
        model.hashing_algorithm = coin_data.hashing_algorithm
        model.categories = coin_data.categories
        model.coingecko_id = coin_data.id
        
        self.repository.session.commit()
    
    def update_existing_currency(self, model: CryptoCurrencyModel, dto: PutCryptoDto):
        coingecko_id = self._find_coingecko_id(dto.name, dto.symbol)
        if coingecko_id is None:
            raise CoingeckoException(f"Coin with name {dto.name} and symbol {dto.symbol} does not exist")
        
        coin_data = self.coingecko_client.get_coin_by_id(coingecko_id)
        
        self.update_currency(model, coin_data)
        self.repository.session.commit()

        return model


    


    