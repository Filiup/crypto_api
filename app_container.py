from dependency_injector import providers, containers
from crypto.crypto_container import CryptoContainer

class AppContainer(containers.DeclarativeContainer):
    crypto = providers.Container(CryptoContainer)

    
