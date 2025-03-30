from dataclasses import dataclass
from db.database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ARRAY

@dataclass
class CryptoCurrencyModel(Base):
    __tablename__ = "crypto_currency"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, unique=True)
    coingecko_id: Mapped[str] = mapped_column(unique=True)
    categories: Mapped[list[str]] = mapped_column(ARRAY(String), server_default="{}")
    symbol: Mapped[str]
    hashing_algorithm: Mapped[str]
    name: Mapped[str]

    def __repr__(self):
        return f"CryptoCurrencyEntity(id={self.id}, symbol={self.symbol}, coingecko_id={self.coingecko_id}, name={self.name})"

