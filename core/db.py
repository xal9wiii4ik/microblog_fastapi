import databases

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://django_user:1234567816@localhost/micro_blog"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_tread': False}
)
database = databases.Database(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()
