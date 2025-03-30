from pydantic import BaseModel, Field


class CreateCryptoDto(BaseModel):
    symbol: str = Field(..., min_length=1, description="Crpyto currency symbol")
    coingecko_id: int = Field(..., description="CoinGecko ID")
    name: str = Field(..., description="Crypto currency name")