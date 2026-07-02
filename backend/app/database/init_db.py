from sqlmodel import SQLModel
from app.models.account import Account
from app.database.session import engine

def create_database():
    SQLModel.metadata.create_all(engine)
