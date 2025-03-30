from pydantic import BaseModel, Field
from crypto.models.cryto_currency_model import CryptoCurrencyModel

class CryptoResponseDto(BaseModel):
    id: int = Field(0, description="Crypto currency ID")
    coingecko_id: str = Field(0, description="CoinGecko ID")
    categories: list[str] = Field(default_factory=list, description="Crypto currency categories")
    symbol: str = Field("BTC",  description="Crypto currency symbol")
    hashing_algorithm: str = Field("SHA256", description="Crypto currency hashing algorithm")
    name: str = Field("Bitcoin", description="Crypto currency name")

    @classmethod
    def from_model(cls, model: CryptoCurrencyModel) -> "CryptoResponseDto":
        return cls(
            id=model.id,
            symbol=model.symbol,
            coingecko_id=model.coingecko_id,
            name=model.name,
            categories=model.categories,
            hashing_algorithm=model.hashing_algorithm
        )

    @classmethod
    def from_model_list(cls, model_list: list[CryptoCurrencyModel]) -> list["CryptoResponseDto"]:
        return [cls.from_model(model) for model in model_list]