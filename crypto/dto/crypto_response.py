from pydantic import BaseModel, Field
from crypto.models.cryto_currency_model import CryptoCurrencyModel

class CryptoResponseDto(BaseModel):
    id: int = Field(0, description="Crypto currency ID")
    coingecko_id: str = Field(0, description="CoinGecko ID")
    categories: list[str] = Field(default_factory=list, description="Crypto currency categories")

    current_price: int = Field(0, description="Current price")
    market_cap: int = Field(0, description="Market cap")
    total_supply: float = Field(0.0, description="Total supply")
    last_updated: str = Field("2025-03-30T20:47:55.499", description="Last updated")
    image_url: str = Field("", description="Crypto currency logo URL")

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
            hashing_algorithm=model.hashing_algorithm,

            current_price=model.current_price,
            market_cap=model.market_cap,
            total_supply=model.total_supply,
            last_updated=model.last_updated.isoformat(),
            logo_url=model.image_url
        )

    @classmethod
    def from_model_list(cls, model_list: list[CryptoCurrencyModel]) -> list["CryptoResponseDto"]:
        return [cls.from_model(model) for model in model_list]