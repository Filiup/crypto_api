from dataclasses import dataclass
from typing import TypedDict


class CoinMarketData(TypedDict):
    current_price: dict[str, int]
    market_cap: dict[str, int]
    total_supply: float
    last_updated: str

class CoinImageUrl(TypedDict):
    thumb: str
    small: str
    large: str

class CoingeckoCoin(TypedDict):
    id: str
    name: str
    symbol: str

class CoingeckoCoinData(CoingeckoCoin):
    hashing_algorithm: str
    categories: list[str]
    market_data: CoinMarketData
    image: CoinImageUrl


@dataclass
class CoinDataResponse:
    id: str
    name: str
    symbol:str
    hashing_algorithm: str
    categories: list[str]
    current_price: float
    market_cap: int
    total_supply: float
    last_updated: str
    image_url: str

    @classmethod
    def from_dict(cls, dict: CoingeckoCoinData):
        return cls(
             id=dict['id'],
             name=dict['name'],
             symbol=dict['symbol'],
             hashing_algorithm=dict['hashing_algorithm'],
             categories=dict['categories'],
             current_price=dict['market_data']['current_price']['czk'],
             market_cap=dict['market_data']['market_cap']["czk"],
             total_supply=dict['market_data']['total_supply'],
             last_updated=dict['market_data']['last_updated'],
             image_url=dict['image']['small']
        )




