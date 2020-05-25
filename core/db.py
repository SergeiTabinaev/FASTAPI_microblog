import databases
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:initeb53@localhost/microblog"

#engine = create_engine(SQLALCHEMY_DATABASE_URL)
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
database = databases.Database(SQLALCHEMY_DATABASE_URL)
Base: DeclarativeMeta = declarative_base()
