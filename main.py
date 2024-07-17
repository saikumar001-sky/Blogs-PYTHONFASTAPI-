from fastapi import FastAPI, HTTPException
from enum import Enum
from typing import Optional
from books import books
from Blog.schemas.blog import Blog,CreateBlog
app = FastAPI()


# ---------------------------------path paramters ------------------
class BookEnum(str, Enum):
    testbook = "Test Book"
    noteBook = "Notes Book"
    ruledBook = "Rules Book"





@app.get("/books/{book_type}")
async def booktypes(book_type: BookEnum):
    if book_type == BookEnum.testbook:
        return HTTPException(status_code=200, detail="this is test book")
    if book_type.value == "Notes Book":
        return HTTPException(status_code=200, detail="this is Notes Book")
    else:
        return HTTPException(status_code=200, detail="No book Found")


# ------------------------- Query Paramters-----------------------


@app.get("/return-books/{book_year}")
async def returnbooks(book_year: int, book_id: int | None = None):
    result_books = []

    if book_id:
        for book in books:
            if book.get("id") == book_id:
                result_books.append(book)
        if len(result_books) > 0:
            return HTTPException(
                status_code=200, detail="success", headers=[result_books, book_year]
            )
        else:
            return HTTPException(
                status_code=404, detail="no data found", headers=result_books
            )

    else:
        return HTTPException(status_code=200, detail="success", headers=books)


@app.post("/blog")
async def create_blog(blog: CreateBlog):
    length = len(books) + 1
    books.append(Blog())
    return HTTPException(status_code=200, detail="success", headers=books)
