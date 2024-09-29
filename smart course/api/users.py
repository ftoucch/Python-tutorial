
from fastapi import APIRouter, Path, Query
from typing import Optional, List
from pydantic import BaseModel

router = APIRouter()


users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str] = None



@router.get("/users", response_model=List[User])
async def get_users():
    return users


@router.post("/users")
async def create_users(user:User):
    users.append(user)
    return "Success"


@router.get("/users/{id}")
async def get_user(id : int):
    return {"user": users[id]}