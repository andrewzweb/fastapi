from fastapi import FastAPI
from fastapi import APIRouter

router = APIRouter()

@router.get("/ping", tags=["ping"])
async def ping_pong():
    return {"message": "pong"}
