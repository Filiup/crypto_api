from pydantic import BaseModel, Field
from crypto.models.cryto_currency_model import CryptoCurrencyModel

class CryptoResponseDto(BaseModel):
    id: int = Field(0, description="Crypto currency ID")
    symbol: str = Field("BTC",  description="Crypto currency symbol")
    coingecko_id: int = Field(0, description="CoinGecko ID")
    name: str = Field("Bitcoin", description="Crypto currency name")

    @classmethod
    def from_model(cls, model: CryptoCurrencyModel) -> "CryptoResponseDto":
        return cls(
            id=model.id,
            symbol=model.symbol,
            coingecko_id=model.coingecko_id,
            name=model.name
        )

    @classmethod
    def from_model_list(cls, model_list: list[CryptoCurrencyModel]) -> list["CryptoResponseDto"]:
        return [cls.from_model(model) for model in model_list]