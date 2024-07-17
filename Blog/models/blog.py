from sqlalchemy import Column, Integer, String
from Blog.db.db import Base


class Blog(Base):
    id: Column(Integer, primary_key=True, index=True)
    title: Column(String)
    description: Column(String)
