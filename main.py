from fastapi import FastAPI

from core.db import database
from routers import routers

from user.logic import jwt_authentication
from core.fast_users import fastapi_users

app = FastAPI()


@app.on_event('startup')
async def startup():
    """Connect to database when server starting"""

    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    """Connect to database when server stopping"""

    await database.disconnect()


app.include_router(routers)
app.include_router(
    fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["users"])


# uvicorn main:app --reload  -  start server
# pip install fastapi\[all\]
# Alembic: alembic init migrations(add file)
# Alembic: alembic revision --autogenerate -m 'commit'
# Alembic: alembic upgrade head -> migrate
