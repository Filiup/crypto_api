from dataclasses import dataclass
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


@dataclass
class CoinDataResponse:
    hashing_algorithm: str
    categories: list[str]
    current_price: float
    market_cap: int
    total_supply: float
    last_updated: str
    logo_url: str




