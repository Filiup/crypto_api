from flask_openapi3 import OpenAPI, Info
from app_container import AppContainer
from dotenv import load_dotenv
from flask import json

from crypto.crypto_view import *
from werkzeug.exceptions import HTTPException

load_dotenv(".env")
load_dotenv(".env.secret", override=True)

def handle_http_error(error: HTTPException):
    print(f"HTTP error: {error.name}")

    response = error.get_response()
    error_dto = ErrorResponseDto(
        status=error.code,
        message=error.name,
        description=error.description
    )

    response.data = json.dumps(error_dto.model_dump())
    response.content_type = "application/json"
    return response


def create_app() -> OpenAPI:
    app_container = AppContainer()
    app_container.wire(modules=[__name__])

    info = Info(title="Crypto API", version="1.0.0")
    app = OpenAPI(__name__, info=info)
    app.register_api_view(crypto_view)
    app.errorhandler(HTTPException)(handle_http_error)

    return app