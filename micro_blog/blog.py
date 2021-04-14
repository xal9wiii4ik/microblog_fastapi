from typing import List

from fastapi import APIRouter, Depends, HTTPException

from core.fast_users import fastapi_users
from user.schemas import User
from . import service
from .schemas import PostCreate, PostList, PostSingle

router = APIRouter()


@router.get(path='/', response_model=List[PostList])
async def post_list():
    """ Get post list """

    return await service.get_post_list()


@router.post(path='/', status_code=201, response_model=PostSingle)
async def post_create(item: PostCreate, user: User = Depends(fastapi_users.get_current_active_user)):
    """ Create post """

    return await service.create_post(item=item, user=user)


@router.get(path='/my_posts', response_model=List[PostList])
async def my_posts(user: User = Depends(fastapi_users.get_current_active_user)):
    """ Get my posts """

    return await service.get_post_list_user(user=user)


@router.get(path='/{pk}', response_model=PostSingle)
async def post_detail(pk: int):
    """ Get post detail """

    post = await service.get_post(pk=pk)
    if post is None:
        return HTTPException(status_code=404, detail='post not found')
    return post


@router.put(path='/{pk}', status_code=200, response_model=PostSingle)
async def post_update(pk: int, item: PostCreate, user: User = Depends(fastapi_users.get_current_active_user)):
    """ Update post """

    post = await service.update_post(pk=pk, item=item, user=user)
    if post is None:
        return HTTPException(status_code=404, detail='post not found')
    return post


@router.get("/children/{pk}", response_model=List[PostList])
async def post_children(pk: int):
    """ Get post children """

    post = await service.get_post_list_children(pk)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.delete(path='/{pk}', status_code=204)
async def post_delete(pk: int, user: User = Depends(fastapi_users.get_current_active_user)):
    """ Delete post """

    return await service.delete_post(pk=pk, user=user)
