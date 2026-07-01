from sqlmodel import SQLModel

from app.database.session import engine

def create_database():
    SQLModel.metadata.create_all(engine)
