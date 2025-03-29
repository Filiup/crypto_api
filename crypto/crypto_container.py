from dependency_injector import containers, providers
from crypto.crypto_service import CryptoService

class CryptoContainer(containers.DeclarativeContainer):
    crypto_service = providers.Singleton(CryptoService)
