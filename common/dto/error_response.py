from pydantic import BaseModel, Field

class ErrorResponseDto(BaseModel):
    status: int = Field(..., description="Status of the response")
    message: str = Field(..., description="Error message")
    description: str = Field(..., description="Detailed error description")