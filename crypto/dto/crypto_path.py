from pydantic import BaseModel, Field

class CryptoPathDto(BaseModel):
    id: int = Field(..., description="Crypto currency id")
    