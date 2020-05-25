# from sqlalchemy.orm import Session
# from .models import Post
from user.models import User
from .models import posts
from .schemas import PostCreate
from core.db import database


async def get_post_list():
    return await database.fetch_all(query=posts.select())


async def create_post(item: PostCreate, user: User):
    post = posts.insert().values(**item.dict(), user=user.id)
    return await database.execute(post)





# def get_post_list(db: Session):
#     return db.query(Post).all()


# def create_post(db: Session, item: PostCreate):
#     post = Post(**item.dict())   #передача item:postcreate как словаря
#     db.add(post)                #записываем в базу данных
#     db.commit()
#     db.refresh(post)
#     return post
