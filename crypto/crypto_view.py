from pydoc import doc
from dependency_injector.wiring import Provide, inject
from flask_openapi3 import APIView, Tag
from app_container import AppContainer
from crypto.crypto_service import CryptoService


crypto_view = APIView(
    url_prefix="/crypto",
    view_tags=[Tag(name="Crypto")]
)

@crypto_view.route("/")
class CryptoListApiView:
    @inject
    def __init__(self, crypto_service: CryptoService = Provide[AppContainer.crypto.crypto_service]):
        self.crypto_service = crypto_service

    @crypto_view.doc(summary="Get all crypto currencies")
    def get(self):
        return self.crypto_service.test()
    
    @crypto_view.doc(summary="Create new crypto currency")
    def post(self):
        return self.crypto_service.test()


