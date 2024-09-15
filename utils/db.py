import os
from sqlmodel import create_engine, Session
from dotenv import load_dotenv

load_dotenv()


database_url: str = os.environ.get("DATABASE_URL") or ""

engine = create_engine(database_url)


async def get_db_connection():
    try:
        session = Session(engine)
        yield session
    finally:
        session.close()
