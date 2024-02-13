from fastapi import FastAPI, status, Response, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI() # create an instance of fastapi

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "post 1", "content": "content of post 1", "id": 1},
            {"title": "post 2", "content": "content of post 2", "id": 2} ]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

@app.get("/") # decorator
def root():
    return {"message": "Hello World!!"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
# def create_post(payLoad: dict = Body(...)):
def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(1, 100000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="post with id: {id} not found")
    return {"post detail": post}

