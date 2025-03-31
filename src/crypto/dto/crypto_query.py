from typing import Optional
from pydantic import BaseModel, Field

class CryptoQueryDto(BaseModel):
    category: Optional[str] =  Field(None, description="Crypto currency category")
    coingecko_id: Optional[str] = Field(None, description="Coingecko id")
    name: Optional[str] = Field(None, description="Crypto currency name")
    symbol: Optional[str] = Field(None, description="Crypto currency symbol")
