from fastapi_users.authentication import JWTAuthentication
from fastapi_users.db import SQLAlchemyUserDatabase

from .models import User
from .schemas import UserDB
from core.db import database

users = User.__table__
user_db = SQLAlchemyUserDatabase(user_db_model=UserDB, database=database, users=users)

SECRET = 'jasdiujdp9832ue3290u328dh1783d102d1uhd'

auth_backends = []

jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600)

auth_backends.append(jwt_authentication)
