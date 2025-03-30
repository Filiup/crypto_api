from typing import TypedDict


class CoinMarketData(TypedDict):
    current_price: dict[str, int]

class CoingeckoCoin(TypedDict):
    id: str
    name: str
    symbol: str

class CoingeckoCoinData(CoingeckoCoin):
    hashing_algorithm: str
    categories: list[str]
    market_data: CoinMarketData