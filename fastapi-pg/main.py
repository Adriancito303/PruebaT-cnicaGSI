from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Text
from uuid import uuid4 as uuid 

app = FastAPI()

posts = []

#Modelo POST
class Post(BaseModel):
    id: Optional[str]
    title: str
    content: Text
    published: bool = False

#Modelo UPDATE
class PostUpdate(BaseModel):
    title: str
    content: str

@app.get("/")
def read_root():
    return {"GSI": "Prueba técnica César Silva"}

#READ
@app.get("/posts") 
def read_posts():
    return posts

@app.get("/posts/{post_id}")
def read_post_id(post_id:str):
    for post in posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404,detail="Post no encontrado")

#CREATE
@app.post("/posts/create")
def create_post(post:Post):
    post.id = str(uuid())
    posts.append(post.dict())
    return {"message":"Post creado"}

#UPDATE
@app.put("/posts/update/{post_id}")
def update_post(post_id:str, updatedPost:PostUpdate):
    for post in posts:
        if post["id"] == post_id:
            post.update(updatedPost.dict())
            return {"message":"Post actualizado"}
    raise HTTPException(status_code=404,detail="Post no encontrado")

#DELETE
@app.delete("/posts/delete/{post_id}")
def delete_post(post_id:str):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts.pop(index)
            return {"message":"Post eliminado"}
    raise HTTPException(status_code=404,detail="Post no encontrado")