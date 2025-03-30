from dataclasses import dataclass
from db.database import Base
from sqlalchemy.orm import Mapped, mapped_column

@dataclass
class CryptoCurrencyModel(Base):
    __tablename__ = "crypto_currency"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, unique=True)
    symbol: Mapped[str] = mapped_column(unique=True)
    coingecko_id: Mapped[str] = mapped_column(unique=True)
    hashing_algorithm: Mapped[str]
    categories: Mapped[list[str]]
    name: Mapped[str]

    def __repr__(self):
        return f"CryptoCurrencyEntity(id={self.id}, symbol={self.symbol}, coingecko_id={self.coingecko_id}, name={self.name})"

