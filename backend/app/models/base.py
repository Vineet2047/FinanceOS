from datetime import UTC, datetime
from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel

class BaseEntity(SQLModel):
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        nullable=False,
    )

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        nullable=False,
    )

    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        nullable=False,
    )
