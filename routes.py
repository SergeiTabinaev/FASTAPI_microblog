# here we are registrated routes and included
from fastapi import APIRouter
from microblog import blog


routes = APIRouter()

routes.include_router(blog.router, prefix="/blog")
