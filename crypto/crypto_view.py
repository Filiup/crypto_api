from dependency_injector.wiring import Provide, inject
from flask import make_response
from flask_openapi3 import APIView, Tag
from app_container import AppContainer
from common.dto.error_response import ErrorResponseDto
from crypto.crypto_service import CryptoService
from crypto.dto.create_crypto import CreateCryptoDto
from crypto.dto.crypto_path import CryptoPathDto
from crypto.dto.crypto_response import CryptoResponseDto
from crypto.dto.crypto_response_list import CryptoResponseListDto
from werkzeug.exceptions import NotFound

from crypto.dto.put_crypto import PutCryptoDto


crypto_view = APIView(
    url_prefix="/crypto",
    view_tags=[Tag(name="Crypto")]
)

@crypto_view.route("/")
class CryptoListApiView:
    @inject
    def __init__(self, crypto_service: CryptoService = Provide[AppContainer.crypto.crypto_service]):
        self.crypto_service = crypto_service

    @crypto_view.doc(summary="Get all crypto currencies", responses={
        200: CryptoResponseListDto,
        400: ErrorResponseDto
    })
    def get(self):
        crypto_currencies = self.crypto_service.getAllCurrencies()
        response_dto = CryptoResponseDto.from_model_list(crypto_currencies)
        response_list_dto = CryptoResponseListDto(root=response_dto)

        return make_response(response_list_dto.model_dump(), 200)
    
    @crypto_view.doc(summary="Create new crypto currency", responses={
        200: CryptoResponseDto,
        400: ErrorResponseDto
    })
    def post(self, body: CreateCryptoDto):
        crypto_currency = self.crypto_service.createCurrency(body)
        response_dto = CryptoResponseDto.from_model(crypto_currency)

        return make_response(response_dto.model_dump(), 200)
    

@crypto_view.route("/<int:id>")
class CryptoApiView:
    @inject
    def __init__(self, crypto_service: CryptoService = Provide[AppContainer.crypto.crypto_service]):
        self.crypto_service = crypto_service

    @crypto_view.doc(summary="Get crypto currency by id", responses={
        200: CryptoResponseDto,
        400: ErrorResponseDto
    })
    def get(self, path: CryptoPathDto):
        crypto_currency = self.crypto_service.getCurrency(path.id)
        if crypto_currency is None:
            raise NotFound(f"Coin with id {path.id} was not found")

        response_dto = CryptoResponseDto.from_model(crypto_currency)
        return make_response(response_dto.model_dump(), 200)
    

    @crypto_view.doc(summary="Delete crypto currency by id", responses={
        200: CryptoResponseDto,
        400: ErrorResponseDto
    })
    def delete(self, path: CryptoPathDto):
        crypto_currency = self.crypto_service.getCurrency(path.id)
        if crypto_currency is None:
            raise NotFound(f"Coin with id {path.id} was not found")

        deleted_currency = self.crypto_service.deleteCurrency(crypto_currency)
        response_dto = CryptoResponseDto.from_model(deleted_currency)

        return make_response(response_dto.model_dump(), 200)
    
    
    @crypto_view.doc(summary="Update crypto by id", responses={
        200: CryptoResponseDto,
        400: ErrorResponseDto
    })
    def put(self, path: CryptoPathDto, body: PutCryptoDto):
        crypto_currency = self.crypto_service.getCurrency(path.id)
        if crypto_currency is None:
            raise NotFound(f"Coin with id {path.id} was not found")

        updated_currency = self.crypto_service.updateCurrency(crypto_currency, body)
        response_dto = CryptoResponseDto.from_model(updated_currency)

        return make_response(response_dto.model_dump(), 200)


      


