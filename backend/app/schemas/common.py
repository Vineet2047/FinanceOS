from datetime import datetime
from typing import Generic, TypeVar
from uuid import UUID
from pydantic import BaseModel
from pydantic.config import ConfigDict

T = TypeVar("T")

class BaseSchema(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
    )

class ApiResponse(BaseModel, Generic[T]):
    success: bool
    message: str
    data: T | None = None


class TimestampSchema(BaseSchema):
    id: UUID
    created_at: datetime
    updated_at: datetime
