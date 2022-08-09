from fastapi import FastAPI
import app.ping.api as ping
from app.db.base import database
from app.endpoints import users

app = FastAPI(title='Exchange')
app.include_router(users.router, prefix="/api/users", tags=["users"])


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(ping.router)
