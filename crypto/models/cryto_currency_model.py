from dataclasses import dataclass
import datetime
from db.database import Base
from sqlalchemy import String, DateTime, BigInteger
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.sql import func

@dataclass
class CryptoCurrencyModel(Base):
    __tablename__ = "crypto_currency"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, unique=True)
    coingecko_id: Mapped[str] = mapped_column(unique=True)
    categories: Mapped[list[str]] = mapped_column(ARRAY(String), server_default="{}")

    current_price: Mapped[int] = mapped_column(BigInteger, nullable=True)
    market_cap: Mapped[int] = mapped_column(BigInteger, nullable=True)
    total_supply: Mapped[float] = mapped_column(nullable=True)
    last_updated: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    image_url: Mapped[str] = mapped_column(nullable=True)

    symbol: Mapped[str]
    hashing_algorithm: Mapped[str]
    name: Mapped[str]

    def __repr__(self):
        return f"CryptoCurrencyEntity(id={self.id}, symbol={self.symbol}, coingecko_id={self.coingecko_id}, name={self.name})"

