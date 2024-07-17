from pydantic import BaseModel

class Blog(BaseModel):
    id: int
    title: str
    author: str
    genre: str
    year: int


class CreateBlog(BaseModel):
    title: str
    author: str
    genre: str
    year: int