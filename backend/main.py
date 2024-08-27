from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify allowed origins here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    if collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    collection.insert_one(user.dict())
    return user

@app.get("/users", response_model=List[User])
def get_users():
    users = list(collection.find({}, {"_id": 0}))
    return users
