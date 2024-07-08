# Database specific implementation of the client
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})

Base = declarative_base()
