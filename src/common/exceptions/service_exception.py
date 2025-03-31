class ServiceException(Exception):
    def __init__(self, message: str, details: str, status_code: int) -> None:
        super().__init__(message)
        self.message = message
        self.details = details
        self.status_code = status_code