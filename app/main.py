from fastapi import FastAPI
from app.api import users

app = FastAPI(title="My FastAPI Service")
app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/")
async def root():
    return {"status": "ok"}
