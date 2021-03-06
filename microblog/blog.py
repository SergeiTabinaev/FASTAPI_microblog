# обычно в main.py мы делаем декоратор @app.get() пишем там функцию для базы url.. но щас по другому
from typing import List
from fastapi import APIRouter, Depends
from core.fast_users import fastapi_users
from user.models import User
# from sqlalchemy.orm import Session
# from core.utils import get_db
from . import service
from . schemas import PostCreate, PostList


router = APIRouter()


@router.get("/", response_model=List[PostList])
async def post_list():
    return await service.get_post_list()


@router.post("/")
async def post_create(item: PostCreate, user: User = Depends(fastapi_users.get_current_active_user)):
    return await service.create_post(item, user)




# this is show posts
# @router.get("/", response_model=List[PostList]) #List - что у нас будет список таких объектов
# def post_list(db: Session = Depends(get_db)): #перед тем как будет запущена ф-я должна быть выполнена зависимость от ф-и get_db из urlsa
#     return service.get_post_list(db)


# this is add post
# в ф-и сначало идет неименованый аргумент потом именованный
# @router.post("/")
# def post_list(item: PostCreate, db: Session = Depends(get_db)): #перед тем как будет запущена ф-я должна быть выполнена зависимость от ф-и get_db из urlsa
#     return service.create_post(db, item)
