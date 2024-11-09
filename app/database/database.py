import os
from dotenv import load_dotenv
from sqlmodel import create_engine, SQLModel

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Configurar el engine con los parámetros específicos para psycopg2
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={
        "options": "-c timezone=utc"
    }
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
