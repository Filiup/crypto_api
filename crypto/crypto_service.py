from crypto.crypto_repository import CryptoRepository
from db import repository

class CryptoService:
    def __init__(self, repository: CryptoRepository):
        self.repository = repository

    def test(self):
        return "hello !!!!"
    


    