from sqlmodel import Field
from app.models.base import BaseEntity

class Account(BaseEntity, table=True):
    __tablename__ = "accounts"

    name: str = Field(
        max_length=100,
        nullable=False,
        unique=True,
        index=True,
    )

    is_active: bool = Field(
        default=True,
        nullable=False,
    )
