from dataclasses import dataclass
import datetime
from db.base_model import Base
from sqlalchemy import String, DateTime, BigInteger, Index

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.sql import func
from sqlalchemy.ext.hybrid import hybrid_property

@dataclass
class CryptoCurrencyModel(Base):
    __tablename__ = "crypto_currency"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, unique=True)
    coingecko_id: Mapped[str] = mapped_column(unique=True, index=True)
    categories: Mapped[list[str]] = mapped_column(ARRAY(String), server_default="{}")

    current_price: Mapped[int] = mapped_column(BigInteger, nullable=True)
    market_cap: Mapped[int] = mapped_column(BigInteger, nullable=True)
    total_supply: Mapped[float] = mapped_column(nullable=True)
    last_updated: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    image_url: Mapped[str] = mapped_column(nullable=True)

    symbol: Mapped[str] = mapped_column(index=True)
    hashing_algorithm: Mapped[str]
    name: Mapped[str] = mapped_column(index=True)

    __table_args__ = (
        Index("idx_crypto_currency_categories_gin", categories, postgresql_using='gin'),
    )

    @hybrid_property
    def identifier(self):
        return self.id

    def __repr__(self):
        return f"CryptoCurrencyEntity(id={self.id}, symbol={self.symbol}, coingecko_id={self.coingecko_id}, name={self.name})"

