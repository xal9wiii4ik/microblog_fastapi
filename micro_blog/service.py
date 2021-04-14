from select import select

from core.db import database
from micro_blog.models import posts, Post
from user.logic import users
from user.models import User
from .schemas import PostCreate


async def get_post_list():
    """ Get post list """

    post_list = await database.fetch_all(query=posts.select().where(posts.c.parent_id.is_(None)))
    return [dict(post) for post in post_list]


async def get_post_list_children(pk: int):
    """ Get post list with children """

    post_list = await database.fetch_all(query=posts.select().where(posts.c.parent_id == pk))
    if post_list is not None:
        return [dict(post) for post in post_list]
    return None


async def get_post(pk: int):
    """ Get post detail """

    user = users.alias('user')
    post = posts.alias('post')
    # we say that take this columns which in select([...]) from table post and user with values (...)
    # TODO: play with alias and label
    query = select([user.c.id.label('userId'), user.c.name.label('userName'), post]) \
        .select_from(post.join(user)).where((post.c.id == pk) & (user.c.id == post.c.user_id))
    post = await database.fetch_one(query=query)
    if post is not None:
        return {**post, 'user': {'id': post.pop('userId'), 'username': post.pop('userName')}}
    return await database.fetch_one(query=posts.select().where(Post.id == pk))


async def get_post_list_user(user: User):
    """ Get user posts """

    posts_list = await database.fetch_all(query=posts.select().where(posts.c.user_id == user.id))
    return [dict(post) for post in posts_list]


async def create_post(item: PostCreate, user: User):
    """ Create post """

    post = posts().insert().values(**item.dict(), user=user)
    pk = await database.execute(post)
    return {**item.dict(), 'pk': pk, 'user': user.id}


async def update_post(pk: int, item: PostCreate, user: User):
    """ Update post """

    post = posts.update().where((posts.c.id == pk) & (posts.c.user_id == user.id)).values(**item.dict())
    return await database.execute(post)


async def delete_post(pk: int, user: User):
    """ Delete post """

    post = posts.delete().where((posts.c.id == pk) & (posts.c.user_id == user.id))
    return await database.execute(post)
