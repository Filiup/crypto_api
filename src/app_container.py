from dependency_injector import providers, containers
from crypto.crypto_container import CryptoContainer
from db.database import Database
import os

class AppContainer(containers.DeclarativeContainer):
    database = providers.Singleton(
        Database,
        url=os.getenv("DATABASE_URL"),
        echo=True if os.getenv("DATABASE_LOGGING") == "true" else False
    )

    session = providers.ThreadLocalSingleton(
        lambda db: db.get_new_session(),
        db=database
    )

    crypto = providers.Container(CryptoContainer, session=session)

    
