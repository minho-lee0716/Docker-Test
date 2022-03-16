from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import env_config

engine = create_engine(env_config['SQLALCHEMY_DATABASE_URI'], echo=True, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def db_conn():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
