from common.exceptions.service_exception import ServiceException

class CryptoNotFoundExpection(ServiceException):
    def __init__(self, details: str) -> None:
        message = "Crypto not found"
        super().__init__(message, details, 404)