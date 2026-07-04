from datetime import UTC, datetime
from uuid import UUID
from app.models.account import Account
from app.repositories.account_repository import AccountRepository
from app.schemas.account import (
    AccountCreate,
    AccountStatusUpdate,
    AccountUpdate,
)

class AccountService:
    def __init__(self, repository: AccountRepository) -> None:
        self._repository = repository

    def create(self, payload: AccountCreate) -> Account:
        name = payload.name.strip()
        existing = self._repository.get_by_name(name)
        if existing:
            raise ValueError("Account already exists.")
        account = Account(
            name=name
        )
        return self._repository.create(account)

    def get_all(self) -> list[Account]:
        return self._repository.get_all()

    def get_by_id(self, account_id: UUID) -> Account:
        account = self._repository.get_by_id(account_id)

        if account is None:
            raise ValueError("Account not found.")

        return account

    def update(
        self,
        account_id: UUID,
        payload: AccountUpdate,
    ) -> Account:
        account = self.get_by_id(account_id)
        name = payload.name.strip()
        duplicate = self._repository.get_by_name(name)
        if duplicate and duplicate.id != account.id:
            raise ValueError("Account name already exists.")
        account.name = name
        account.updated_at = datetime.now(UTC)
        return self._repository.save(account)

    def update_status(
        self,
        account_id: UUID,
        payload: AccountStatusUpdate,
    ) -> Account:
        account = self.get_by_id(account_id)
        account.is_active = payload.is_active
        account.updated_at = datetime.now(UTC)
        return self._repository.save(account)
