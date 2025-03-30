from typing import List
from pydantic import RootModel
from crypto.dto.crypto_response import CryptoResponseDto

class CryptoResponseListDto(RootModel):
    root: List[CryptoResponseDto]

