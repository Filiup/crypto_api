from pydantic import BaseModel, Field

class PutCryptoDto(BaseModel):
    symbol: str = Field(..., min_length=1, description="Crypto currency symbol")
    name: str = Field(..., description="Crypto currency name")