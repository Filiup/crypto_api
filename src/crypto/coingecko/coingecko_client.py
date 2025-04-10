from .types import CoinDataResponse, CoingeckoCoin, CoingeckoCoinData
import requests

class CoinGeckoClient:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url

    def get_all_coins(self) -> list[CoingeckoCoin]:
        url = f"{self.base_url}/coins/list"
        headers = {
            "accept": "application/json",
            "x-cg-demo-api-key": self.api_key
        }
        response = requests.get(url, headers=headers)
        return response.json()

    def get_coin_by_id(self, coin_id: str) -> CoinDataResponse:
        url = f"{self.base_url}/coins/{coin_id}"
        headers = {
            "accept": "application/json",
            "x-cg-demo-api-key": self.api_key
        }

        response = requests.get(url, headers=headers)
        json: CoingeckoCoinData = response.json()

        return CoinDataResponse.from_dict(json)

