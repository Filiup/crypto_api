from common.exceptions.service_exception import ServiceException

class CoingeckoException(ServiceException):
    def __init__(self, details: str):
        message = "Coingecko exception"
        super().__init__(message, details, 400)