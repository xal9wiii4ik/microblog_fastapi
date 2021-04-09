from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://django_user:1234567816@localhost/micro_blog"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Alembic: alembic init migrations(add file)
# alembic revision --autogenerate -m 'commit'
# Alembic : alembic upgrade head -> migrate
