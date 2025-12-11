from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class UserIn(BaseModel):
    name: str

class UserOut(UserIn):
    id: int

# in-memory store (for demo)
_users = [{"id": 1, "name": "Alice"}]
_next_id = 2

@router.get("/", response_model=List[UserOut])
async def list_users():
    return _users

@router.post("/", response_model=UserOut, status_code=201)
async def create_user(user: UserIn):
    global _next_id
    if not user.name.strip():
        raise HTTPException(status_code=400, detail="name required")
    new_user = {"id": _next_id, "name": user.name}
    _users.append(new_user)
    _next_id += 1
    return new_user
