from pydantic import Field
from app.schemas.common import ApiResponse, BaseSchema, TimestampSchema

class AccountCreate(BaseSchema):
    name: str = Field(
        min_length=1,
        max_length=100,
    )

class AccountUpdate(BaseSchema):
    name: str = Field(
        min_length=1,
        max_length=100,
    )

class AccountStatusUpdate(BaseSchema):
    is_active: bool

class AccountRead(TimestampSchema):
    name: str
    is_active: bool

class AccountResponse(ApiResponse[AccountRead]):
    pass

class AccountListResponse(ApiResponse[list[AccountRead]]):
    pass
