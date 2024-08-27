from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from typing import List

app = FastAPI()

# MongoDB Client
client = MongoClient('mongodb://mongodb-service:27017/')
db = client.registration_db
collection = db.users

class User(BaseModel):
    name: str
    email: str
    password: str

@app.post("/register", response_model=User)
def register_user(user: User):
    user_dict = user.dict()
    if collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    collection.insert_one(user_dict)
    return user

@app.get("/users", response_model=List[User])
def get_users():
    users = list(collection.find({}, {"_id": 0}))
    return users
