from typing import List
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

    
while True:
    
    try:
        conn = psycopg2.connect(host = "localhost", database = "fastapi", user = "postgres", 
                                password = "password123", cursor_factory=RealDictCursor) # Connect to database
        cursor = conn.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        print("Connection to database failed")
        print("Error: ", error)
        time.sleep(3)


my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite foods", "content": "I like pizza", "id": 2}]


def find_post(id): 
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i


app.include_router(post.router) # Include the router from the post.py file
app.include_router(user.router) # Include the router from the user.py file
app.include_router(auth.router) # Include the router from the auth.py file

@app.get("/")
def root():
    return {"message": "Hello World"}




