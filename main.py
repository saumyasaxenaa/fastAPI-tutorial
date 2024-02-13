from fastapi import FastAPI

app = FastAPI() # create an instance of fastapi

@app.get("/") # decorator
def root():
    return {"message": "Hello World!!"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}