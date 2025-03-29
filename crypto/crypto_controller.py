from dependency_injector.wiring import Provide, inject
from flask import Blueprint

from app_container import AppContainer
from crypto.crypto_service import CryptoService

crypto_blueprint = Blueprint("crypto_controller", __name__)

@crypto_blueprint.route("/", methods=["GET"])
@inject
def index(crypto_service: CryptoService = Provide[AppContainer.crypto.crypto_service]):
    return crypto_service.test()

