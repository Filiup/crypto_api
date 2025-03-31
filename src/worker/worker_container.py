import os
from dependency_injector import providers, containers
from crypto.coingecko.coingecko_client import CoinGeckoClient
from crypto.crypto_repository import CryptoRepository
from db.database import Database


class WorkerContainer(containers.DeclarativeContainer):
    database = providers.Singleton(
        Database,
        url=os.getenv("DATABASE_URL")
    )

    session = providers.Factory(
        lambda db: db.get_session(),
        db=database
    )

    crypto_repository = providers.Singleton(CryptoRepository, session=session)


    coingecko_client = providers.Singleton(
        CoinGeckoClient, 
        api_key=os.getenv("COINGECKO_API_KEY"),
        base_url=os.getenv("COINGECKO_BASE_URL")
    )

