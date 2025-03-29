from flask_openapi3 import OpenAPI, Info
from app_container import AppContainer
from dotenv import load_dotenv

from crypto.crypto_view import *

load_dotenv()


def create_app() -> OpenAPI:
    app_container = AppContainer()
    app_container.wire(modules=[__name__])

    info = Info(title="Crypto API", version="1.0.0")
    app = OpenAPI(__name__, info=info)
    app.register_api_view(crypto_view)
    return app