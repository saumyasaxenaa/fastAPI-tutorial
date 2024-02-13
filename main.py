from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI() # create an instance of fastapi

@app.get("/") # decorator
def root():
    return {"message": "Hello World!!"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/createposts")
def create_post(payLoad: dict = Body(...)):
    print(payLoad)
    return {"new_post": f"title: {payLoad['title']} content: {payLoad['content']}"}
# title: str, content: str