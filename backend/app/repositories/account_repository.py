from uuid import UUID
from sqlmodel import select
from app.models.account import Account
from app.repositories.base_repository import BaseRepository

class AccountRepository(BaseRepository):
    def create(self, account: Account) -> Account:
        self._session.add(account)
        self._session.commit()
        self._session.refresh(account)
        return account

    def get_all(self) -> list[Account]:
        statement = select(Account).order_by(Account.name)
        return list(self._session.exec(statement).all())

    def get_by_id(self, account_id: UUID) -> Account | None:
        statement = select(Account).where(Account.id == account_id)
        return self._session.exec(statement).first()

    def get_by_name(self, name: str) -> Account | None:
        statement = select(Account).where(Account.name == name)
        return self._session.exec(statement).first()

    def save(self, account: Account) -> Account:
        self._session.add(account)
        self._session.commit()
        self._session.refresh(account)
        return account
