from dependency_injector import containers, providers
from crypto.crypto_repository import CryptoRepository
from crypto.crypto_service import CryptoService
from .coingecko import CoinGeckoClient
import os



class CryptoContainer(containers.DeclarativeContainer):
    session = providers.Dependency()

    crypto_repository = providers.Singleton(CryptoRepository, session=session)

    coingecko_client = providers.Singleton(
        CoinGeckoClient, 
        api_key=os.getenv("COINGECKO_API_KEY"),
        base_url=os.getenv("COINGECKO_BASE_URL")
    )
                                           
    crypto_service = providers.Singleton(
        CryptoService, 
        repository=crypto_repository,
        coingecko_client=coingecko_client
    )
