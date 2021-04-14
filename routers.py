from fastapi import APIRouter

from micro_blog import blog


routers = APIRouter()

routers.include_router(blog.router, prefix='/blog')

