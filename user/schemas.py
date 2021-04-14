import uuid
import pydantic

from typing import Optional

from fastapi_users import models


class User(models.BaseUser):
    """ Using for base model """

    pass


class UserInPost(models.BaseModel):
    """ For getting user when we getting post detail or list """

    int: Optional[str]
    username: str = ''

    @pydantic.validator('id', pre=True, always=True, check_fields=False)
    def default_id(cls, value):
        return value or str(uuid.uuid4())

    class Config:
        orm_mode = True


class UserCreate(models.BaseUserCreate):
    """ Schema for user create """

    username: str


class UserUpdate(models.BaseUserUpdate):
    """ Schema for user update """

    pass


class UserDB(User, models.BaseUserDB):
    """ Schema for user to db """

    pass
