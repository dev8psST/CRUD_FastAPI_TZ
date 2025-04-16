from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
import databases
import pymysql
from databases import Database
from db import *

# Database connection URL
DATABASE_URL = "mysql+pymysql://root:password@localhost/test"

# FastAPI app instance
app = FastAPI()

# Database connection instance
database = Database(DATABASE_URL)

# Define Pydantic model for User
class Post(BaseModel):

    title: str
    content: str
    author_id: int
    category_id: int
    tag_id: int


class Author(BaseModel):

    name: str


class Tag(BaseModel):

    name: str


class Category(BaseModel):

    name: str


# API Router instance
router = APIRouter()

# Connect to the database
@app.on_event("startup")
async def startup():
    await database.connect()


# Disconnect from the database
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@router.post("/posts/")
async def create_post(post: Post):
    query = "INSERT INTO posts(title, content, author_id, category_id, tag_id)\
             VALUES (:title, :content, :author_id, :category_id, :tag_id)"
    values = post.dict()
    await database.execute(query=query, values=values)
    return {"message": "Post created successfully"}


# Get category by ID endpoint
@router.post("/categories/")
async def create_category(category: Category):
    query = "INSERT INTO categories(name) VALUES (:name)"
    values = category.dict()
    await database.execute(query=query, values=values)
    return {"message": "Category created successfully"}


# Get author by ID endpoint
@router.post("/authors/")
async def create_author(author: Author):
    query = "INSERT INTO authors(name) VALUES (:name)"
    values = author.dict()
    await database.execute(query=query, values=values)
    return {"message": "Author created successfully"}


# Get tag by ID endpoint
@router.post("/tags/")
async def create_tag(tag: Tag):
    query = "INSERT INTO tags(name) VALUES (:name)"
    values = tag.dict()
    await database.execute(query=query, values=values)
    return {"message": "Tag created successfully"}


# Get post by ID endpoint
@router.get("/posts/{post_id}")
async def get_post(post_id: int):
    query = "SELECT * FROM posts WHERE id = :id"
    post = await database.fetch_one(query=query, values={"id": post_id})
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

# Get aurhor by ID endpoint
@router.get("/authors/{author_id}")
async def get_authors(author_id: int):
    query = "SELECT * FROM authors WHERE id = :id"
    get = await database.fetch_one(query=query, values={"id": author_id})
    if get is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return get

# Update post endpoint
@router.put("/posts/{post_id}")
async def update_post(post_id: int, post: Post):
    query = "SELECT * FROM posts WHERE id = :id"
    pp = await database.fetch_one(query=query, values={"id": post_id})

    if pp is None:
        raise HTTPException(status_code=404, detail="Post not found")

    query_up = "UPDATE posts SET title=:title, content=:content, author_id=:author_id,\
             category_id=:category_id, tag_id=:tag_id \
             WHERE id=:id"
    values_up = {"id": post_id, **post.dict()}
    await database.execute(query=query_up, values=values_up)
    return {"message": "Post updated successfully"}


# Delete post
@app.delete("/posts/{post_id}")
async def delete_post(post_id: int):
    query = "SELECT * FROM posts WHERE id = :id"
    query_del = "DELETE FROM posts WHERE id = :id"
    values = {"id": post_id}
    post = await database.fetch_one(query=query, values={"id": post_id})
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    else:
        await database.execute(query=query_del, values=values)

    return {"message": "Post deleted successfully"}


app.include_router(router)
