import os
from dotenv import load_dotenv
from sqlmodel import create_engine, select, SQLModel

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")  # Por ejemplo: postgres://user:password@localhost/dbname

sql_url = DATABASE_URL

connect_args = {"check_same_thread": False}
engine = create_engine(sql_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
