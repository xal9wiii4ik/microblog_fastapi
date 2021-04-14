from sqlalchemy import (
    Column,
    String,
    DateTime,
)
from fastapi_users.db import SQLAlchemyBaseUserTable
from core.db import Base


class User(Base, SQLAlchemyBaseUserTable):
    """ Base user model """

    username = Column(String, unique=True)
    date = Column(DateTime)


users = User.__table__
