from dependency_injector import containers, providers
from crypto.crypto_repository import CryptoRepository
from crypto.crypto_service import CryptoService

class CryptoContainer(containers.DeclarativeContainer):
    session = providers.Dependency()

    crypto_repository = providers.Singleton(CryptoRepository, session=session)
    crypto_service = providers.Singleton(CryptoService, repository=crypto_repository)
