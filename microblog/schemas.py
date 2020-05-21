from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):
    title: str
    text: str
    date: datetime

    class Config:            # like to queryset.. need for take data in DB
        orm_mode = True


class PostList(PostBase):
    id: int



class PostCreate(PostBase):
    pass
