from pydantic import BaseModel

from typing import Optional

from datetime import datetime

from user.schemas import UserInPost


class PostBase(BaseModel):
    """ Schema for post base """

    title: str = ''
    text: str = ''
    date: Optional[datetime]


class PostParent(PostBase):
    """ Schema for post parent """

    id: Optional[int]

    class Config:
        orm_mode = True


class PostList(PostBase):
    """ Schema for post list """

    id: Optional[int]
    user: UserInPost


class PostSingle(PostList):
    """ Schema for post detail """

    pass


class PostCreate(PostBase):
    """ Schema for post create """

    parent_id: Optional[int] = None

    class Config:
        # we say that create this in database
        # we include this in class where we want to take info(  relationship)
        orm_mode = True
