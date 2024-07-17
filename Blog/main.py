from fastapi import FastAPI
from Blog.schemas.blog import CreateBlog

app = FastAPI()


@app.post("/blog")
async def create(blog: CreateBlog):
    return blog
