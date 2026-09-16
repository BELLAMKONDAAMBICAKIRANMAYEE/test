from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, DeclarativeBase


DATABASE_URL = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="admin@123",
    host="localhost",
    database="ats_db"
)


engine = create_engine(
    DATABASE_URL,
    echo=True
)


LocalSession = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

def get_db():

    db = LocalSession()

    try:
        yield db

    finally:
        db.close()
class Base(DeclarativeBase):
    pass