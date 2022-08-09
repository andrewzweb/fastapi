from databases import Database
from sqlalchemy import create_engine, MetaData
from app.core.config import FA_DATABASE_URL

database = Database(FA_DATABASE_URL)
metadata = MetaData()

engine = create_engine(
    FA_DATABASE_URL,
)
