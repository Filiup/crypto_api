from common.exceptions.service_exception import ServiceException


class DatabaseException(ServiceException):
    def __init__(self, details: str):
        message = "Database exception"
        super().__init__(message, details, 400)

    