from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase


# DATABASE_URL="mysql+pymysql://<user>:<password>@<host>/"
DATABASE_URL="mysql+pymysql://root:<password>@localhost/ats_db/"
engine=create_engine(DATABASE_URL)
LocalSession=sessionmaker(bind=engine,autocommit=False,autoflush=False)

class Base(DeclarativeBase):
    pass