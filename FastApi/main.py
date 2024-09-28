from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str


@app.get("/")
def root():
    return {"message": "Hello to my World"}

@app.get("/posts")
def get_posts():
    return {"Data" : "This is your post"}

@app.post("/createposts")
def create_posts(new_post:Post):
    print(new_post.title)
    return {"new_post" : "new Post"} 