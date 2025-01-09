from sqlmodel import SQLModel, create_engine
from models import News

sqlite_filename = 'news.db'
engine = create_engine(f'sqlite:///{sqlite_filename}', echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
